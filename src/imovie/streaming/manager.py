# -*- coding: utf-8 -*-
"""
streaming manager module.
"""

import os

from time import sleep

from flask import send_from_directory

import pyrin.globalization.datetime.services as datetime_services
import pyrin.configuration.services as config_services
import pyrin.utils.path as path_utils

from pyrin.core.globals import _
from pyrin.core.structs import Manager, Context

import imovie.movies.services as movie_services
import imovie.movies.collector.services as movie_collector_services
import imovie.movies.root.services as movie_root_services

from imovie.streaming import StreamingPackage
from imovie.streaming.enumerations import TranscodingStatusEnum, StreamProviderEnum
from imovie.streaming.interface import AbstractStreamProvider
from imovie.streaming.exceptions import StreamDirectoryNotExistedError, \
    InvalidTranscodingStatusError, InvalidStreamProviderTypeError, \
    StreamProviderDoesNotExistError, DuplicateStreamProviderError, StreamDoesNotExistError


class StreamingManager(Manager):
    """
    streaming manager class.
    """

    package_class = StreamingPackage

    # how many seconds to wait after starting transcoding.
    SLEEP_SECONDS = 4

    def __init__(self):
        """
        initializes an instance of StreamingManager.
        """

        super().__init__()

        # a dict containing all registered stream providers. in the form of:
        # {str name: AbstractStreamProvider instance}
        self._providers = Context()
        self._threads = config_services.get('streaming', 'transcoding', 'threads')
        self._preset = config_services.get('streaming', 'transcoding', 'preset')
        self._stream_directory = config_services.get('streaming', 'general', 'directory')
        self._create_stream_directory(self._stream_directory)

    def _create_stream_directory(self, directory):
        """
        creates the given stream directory.

        :param str directory: stream directory path.
        """

        path_utils.create_directory(directory, ignore_existed=True)

    def _is_failed(self, directory):
        """
        gets a value indicating that given stream directory transcoding is failed.

        :param str directory: directory path of stream.

        :rtype: bool
        """

        failed_file = self._get_status_file_name(directory, TranscodingStatusEnum.FAILED)
        return os.path.exists(failed_file)

    def _is_started(self, directory):
        """
        gets a value indicating that given stream directory transcoding is started.

        :param str directory: directory path of stream.

        :rtype: bool
        """

        started_file = self._get_status_file_name(directory, TranscodingStatusEnum.STARTED)
        return os.path.exists(started_file)

    def _is_finished(self, directory):
        """
        gets a value indicating that given stream directory transcoding is finished.

        :param str directory: directory path of stream.

        :rtype: bool
        """

        finished_file = self._get_status_file_name(directory, TranscodingStatusEnum.FINISHED)
        return os.path.exists(finished_file)

    def _set_status(self, directory, status):
        """
        sets the transcoding status of given stream directory.

        :param str directory: directory path of stream.
        :param str status: status of transcoding.
        :enum status:
            NOT_AVAILABLE = 'not_available'
            STARTED = 'started'
            FINISHED = 'finished'
            FAILED = 'failed'

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        :raises InvalidTranscodingStatusError: invalid transcoding status error.
        """

        if not self.exists(directory):
            raise StreamDirectoryNotExistedError('Stream directory [{directory}] does not exist.'
                                                 .format(directory=directory))

        if status not in TranscodingStatusEnum:
            raise InvalidTranscodingStatusError('Transcoding status [{status}] is invalid.'
                                                .format(status=status))

        file_name = self._get_status_file_name(directory, status)
        with open(file_name, mode='w') as file:
            now = datetime_services.get_current_timestamp()
            file.write(now)

    def _get_status_file_name(self, directory, status):
        """
        gets the file name of given status in given stream directory.

        :param str directory: directory path of stream.
        :param str status: status of transcoding.
        :enum status:
            NOT_AVAILABLE = 'not_available'
            STARTED = 'started'
            FINISHED = 'finished'
            FAILED = 'failed'
        """

        return os.path.join(directory, status)

    def _get_stream_provider(self, name):
        """
        gets the stream provider with given name.

        it raises an error if stream provider does not exist.

        :param str name: stream provider name.

        :raises StreamProviderDoesNotExistError: stream provider does not exist error.

        :rtype: AbstractStreamProvider
        """

        if name not in self._providers:
            raise StreamProviderDoesNotExistError('Stream provider with name [{name}] '
                                                  'does not exist.'.format(name=name))

        return self._providers.get(name)

    def _get_stream_path(self, movie_id):
        """
        gets the stream path for given movie.

        :param uuid.UUID movie_id: movie id.
        """

        return os.path.join(self._stream_directory, str(movie_id))

    def _transcode(self, movie_id, **options):
        """
        transcodes a movie file to stream directory.

        it returns a tuple of two items. first item is the stream directory
        path and the second item is the output file name.

        if the stream is already present and is usable, it returns the available
        stream and bypasses the transcoding.

        :param uuid.UUID movie_id: movie id to be transcoded.

        :keyword str subtitle: subtitle file path.
        :keyword int threads: number of threads to be used.
        :keyword str preset: transcoding preset name.

        :raises TranscodeError: transcode error.

        :returns: tuple[str stream_directory, str output_file]
        :rtype: tuple[str, str]
        """

        stream_path = self._get_stream_path(movie_id)
        stream = self._get_stream_provider(StreamProviderEnum.DASH)
        status = self.get_status(stream_path)
        if status in (TranscodingStatusEnum.STARTED,
                      TranscodingStatusEnum.FINISHED):
            return stream_path, stream.output_file

        path_utils.remove_directory(stream_path)
        movie = movie_services.get(movie_id)
        paths = movie_root_services.get_full_path(movie.directory_name)
        if not paths:
            raise Exception('No movie found.')

        SINGLE_PATH = paths[0]
        FILES = movie_collector_services.get_movie_files(SINGLE_PATH, force=movie.forced)

        if not FILES:
            raise Exception('No movie files found.')

        SINGLE_FILE = FILES[0]

        self._create_stream_directory(stream_path)
        options.update(threads=self._threads, preset=self._preset)
        stream.transcode(SINGLE_FILE, stream_path, **options)

        # we have to wait here for manifest file to become available.
        sleep(self.SLEEP_SECONDS)

        return stream_path, stream.output_file

    def _send_stream(self, stream, file, **options):
        """
        sends given file from given stream to client.

        :param str stream: stream directory.
        :param str file: file name to be returned.

        :raises StreamDoesNotExistError: stream does not exist error.

        :rtype: bytes
        """

        full_path = os.path.join(stream, file)
        if not os.path.exists(full_path):
            raise StreamDoesNotExistError(_('Stream [{stream}] does not exist.')
                                          .format(stream=full_path))

        options.update(conditional=True)
        return send_from_directory(stream, file, **options)

    def register_stream_provider(self, instance, **options):
        """
        registers the given stream provider.

        :param AbstractStreamProvider instance: stream provider instance.

        :raises InvalidStreamProviderTypeError: invalid stream provider type error.
        :raises DuplicateStreamProviderError: duplicate stream provider error.
        """

        if not isinstance(instance, AbstractStreamProvider):
            raise InvalidStreamProviderTypeError('Input parameter [{instance}] is '
                                                 'not an instance of [{base}].'
                                                 .format(instance=instance,
                                                         base=AbstractStreamProvider))

        if instance.name in self._providers:
            raise DuplicateStreamProviderError('There is another registered stream '
                                               'provider with name [{name}].'
                                               .format(name=instance.name))

        self._providers[instance.name] = instance

    def get_provider_names(self):
        """
        gets the name of all registered stream providers.

        :rtype: list[str]
        """

        return list(self._providers.keys())

    def exists(self, directory):
        """
        gets a value indicating that given stream directory exists.

        :param str directory: directory path of stream.

        :raises InvalidPathError: invalid path error.
        :raises PathIsNotAbsoluteError: path is not absolute error.

        :rtype: bool
        """

        return path_utils.exists(directory)

    def get_status(self, directory):
        """
        gets the transcoding status of given stream directory.

        :param str directory: directory path of stream.

        :rtype: str
        """

        if not self.exists(directory):
            return TranscodingStatusEnum.NOT_AVAILABLE

        if self._is_failed(directory):
            return TranscodingStatusEnum.FAILED

        if self._is_finished(directory):
            return TranscodingStatusEnum.FINISHED

        if self._is_started(directory):
            return TranscodingStatusEnum.STARTED

        return TranscodingStatusEnum.NOT_AVAILABLE

    def set_started(self, directory):
        """
        sets the given stream as started transcoding.

        :param str directory: directory path of stream.
        """

        self._set_status(directory, TranscodingStatusEnum.STARTED)

    def set_finished(self, directory):
        """
        sets the given stream as finished transcoding.

        :param str directory: directory path of stream.
        """

        self._set_status(directory, TranscodingStatusEnum.FINISHED)

    def set_failed(self, directory):
        """
        sets the given stream as failed transcoding.

        :param str directory: directory path of stream.
        """

        self._set_status(directory, TranscodingStatusEnum.FAILED)

    def set_process_id(self, directory, process_id):
        """
        sets the ffmpeg process id for given stream.

        :param str directory: directory path of stream.
        :param int process_id: ffmpeg process id.

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        """

        if not self.exists(directory):
            raise StreamDirectoryNotExistedError('Stream directory [{directory}] does not exist.'
                                                 .format(directory=directory))

        file_name = os.path.join(directory, 'pid')
        with open(file_name, mode='w') as file:
            file.write(str(process_id))

    def start_stream(self, movie_id, **options):
        """
        starts streaming of given movie.

        it returns the related manifest file of the stream.

        :param uuid.UUID movie_id: movie id to be streamed.

        :keyword str subtitle: subtitle file path.
        :keyword int threads: number of threads to be used.
        :keyword str preset: transcoding preset name.

        :raises TranscodeError: transcode error.
        :raises StreamDoesNotExistError: stream does not exist error.

        :rtype: bytes
        """

        directory, file = self._transcode(movie_id, **options)
        return self._send_stream(directory, file)

    def continue_stream(self, movie_id, file, **options):
        """
        continues the streaming of given movie id.

        :param uuid.UUID movie_id: movie id to be streamed.
        :param str file: stream file name to be returned.

        :raises StreamDoesNotExistError: stream does not exist error.

        :rtype: bytes
        """

        directory = self._get_stream_path(movie_id)
        return self._send_stream(directory, file)
