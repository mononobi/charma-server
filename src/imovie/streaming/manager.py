# -*- coding: utf-8 -*-
"""
streaming manager module.
"""

import os
import time

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
import imovie.subtitles.services as subtitle_services

from imovie.streaming import StreamingPackage
from imovie.streaming.enumerations import TranscodingStatusEnum, StreamProviderEnum
from imovie.streaming.interface import AbstractStreamProvider
from imovie.streaming.exceptions import StreamDirectoryNotExistedError, \
    InvalidTranscodingStatusError, InvalidStreamProviderTypeError, \
    StreamProviderDoesNotExistError, DuplicateStreamProviderError, StreamDoesNotExistError, \
    MovieDirectoryNotFoundError, MultipleMovieDirectoriesFoundError, MovieFileNotFoundError, \
    MultipleMovieFilesFoundError


class StreamingManager(Manager):
    """
    streaming manager class.
    """

    package_class = StreamingPackage

    # how many seconds to wait for manifest file on each try.
    INTERVAL = 1

    # how many times to check for manifest file creation before giving up.
    RETRY = 20

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

    def _set_status(self, directory, status, **options):
        """
        sets the transcoding status of given stream directory.

        :param str directory: directory path of stream.
        :param str status: status of transcoding.
        :enum status:
            NOT_AVAILABLE = 'not_available'
            STARTED = 'started'
            FINISHED = 'finished'
            FAILED = 'failed'

        :keyword str message: message to be written to file.

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        :raises InvalidTranscodingStatusError: invalid transcoding status error.
        """

        if not self.exists(directory):
            raise StreamDirectoryNotExistedError('Stream directory [{directory}] does not exist.'
                                                 .format(directory=directory))

        if status not in TranscodingStatusEnum:
            raise InvalidTranscodingStatusError('Transcoding status [{status}] is invalid.'
                                                .format(status=status))

        message = options.get('message')
        file_name = self._get_status_file_name(directory, status)
        with open(file_name, mode='w') as file:
            now = datetime_services.get_current_timestamp()
            file.write(now)
            if message not in (None, ''):
                message = '\n{message}'.format(message=message)
                file.write(message)

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

    def _get_movie_directory(self, movie_id, **options):
        """
        gets given movie's directory path if possible.

        :param uuid.UUID movie_id: movie id to get its directory path.

        :keyword str directory: movie directory path.
                                it will only be used if more than
                                one directory found for given movie.

        :raises MovieDirectoryNotFoundError: movie directory not found error.
        :raises MultipleMovieDirectoriesFoundError: multiple movie directories found error.

        :rtype: str
        """

        movie = movie_services.get(movie_id)
        movie_paths = movie_root_services.get_full_path(movie.directory_name)
        if not movie_paths:
            raise MovieDirectoryNotFoundError(_('Movie directory [{directory}] not found.')
                                              .format(directory=movie.directory_name))

        found_directory = None
        if len(movie_paths) > 1:
            directory = options.get('directory')
            if directory in movie_paths:
                found_directory = directory
        else:
            found_directory = movie_paths[0]

        if found_directory is None:
            raise MultipleMovieDirectoriesFoundError(_('Multiple movie directories '
                                                       'found for movie [{directory}].')
                                                     .format(directory=movie.directory_name))

        return found_directory

    def _get_movie_file(self, movie_id, directory_path, **options):
        """
        gets given movie's file path if possible.

        :param uuid.UUID movie_id: movie id to get its file path.
        :param str directory_path: movie directory path.

        :keyword str file: movie file path.
                           it will only be used if more than
                           one file found for given movie.

        :raises MovieFileNotFoundError: movie file not found error.
        :raises MultipleMovieFilesFoundError: multiple movie files found error.

        :rtype: str
        """

        movie = movie_services.get(movie_id)
        movie_files = movie_collector_services.get_movie_files(directory_path,
                                                               force=movie.forced)

        if not movie_files:
            raise MovieFileNotFoundError(_('No movie files found for movie [{directory}].')
                                         .format(directory=movie.directory_name))

        found_file = None
        if len(movie_files) > 1:
            file = options.get('file')
            if file in movie_files:
                found_file = file
        else:
            found_file = movie_files[0]

        if found_file is None:
            raise MultipleMovieFilesFoundError(_('Multiple movie files found '
                                                 'for movie [{directory}].')
                                               .format(directory=movie.directory_name))

        return found_file

    def _transcode(self, movie_id, **options):
        """
        transcodes a movie file to stream directory.

        it returns a tuple of two items. first item is the stream directory
        path and the second item is the output file name.

        if the stream is already present and is usable, it returns the available
        stream and bypasses the transcoding.

        :param uuid.UUID movie_id: movie id to be transcoded.

        :keyword str directory: movie directory path.
                                it will only be used if more than
                                one directory found for given movie.

        :keyword str file: movie file path.
                           it will only be used if more than
                           one file found for given movie.

        :raises MovieDirectoryNotFoundError: movie directory not found error.
        :raises MultipleMovieDirectoriesFoundError: multiple movie directories found error.
        :raises MovieFileNotFoundError: movie file not found error.
        :raises MultipleMovieFilesFoundError: multiple movie files found error.

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
        found_directory = self._get_movie_directory(movie_id, **options)
        found_file = self._get_movie_file(movie_id, found_directory, **options)
        subtitles = subtitle_services.get_subtitles(found_directory)
        self._create_stream_directory(stream_path)
        options.update(threads=self._threads, preset=self._preset, subtitles=subtitles)
        stream.transcode(found_file, stream_path, **options)

        # we have to wait here for manifest file to become available.
        self._wait_for_manifest(stream_path, stream.output_file,
                                self.RETRY, self.INTERVAL)

        return stream_path, stream.output_file

    def _wait_for_manifest(self, stream_path, manifest, retry, interval):
        """
        sleeps current thread and checks if manifest file is created on specific intervals.

        :param str stream_path: stream directory path to look for manifest file.
        :param str manifest: manifest file name.
        :param int retry: number of retries to check if manifest file is created.
        :param float interval: number of seconds to wait between each interval.
        """

        full_path = os.path.join(stream_path, manifest)
        while not path_utils.exists(full_path) and retry > 0:
            retry -= 1
            sleep(interval)

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

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        """

        self._set_status(directory, TranscodingStatusEnum.STARTED)

    def set_finished(self, directory):
        """
        sets the given stream as finished transcoding.

        :param str directory: directory path of stream.

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        """

        self._set_status(directory, TranscodingStatusEnum.FINISHED)

    def set_failed(self, directory, error):
        """
        sets the given stream as failed transcoding.

        :param str directory: directory path of stream.
        :param str error: error message.

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        """

        self._set_status(directory, TranscodingStatusEnum.FAILED, message=error)

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

    def set_access_time(self, directory):
        """
        sets the last access time for given stream.

        :param str directory: directory path of stream.

        :raises StreamDirectoryNotExistedError: stream directory not existed error.
        """

        if not self.exists(directory):
            raise StreamDirectoryNotExistedError('Stream directory [{directory}] does not exist.'
                                                 .format(directory=directory))

        file_name = os.path.join(directory, 'access')
        with open(file_name, mode='w') as file:
            file.write(str(time.time()))

    def start_stream(self, movie_id, **options):
        """
        starts streaming of given movie.

        it returns the related manifest file of the stream.

        :param uuid.UUID movie_id: movie id to be streamed.

        :raises MovieDirectoryNotFoundError: movie directory not found error.
        :raises MultipleMovieDirectoriesFoundError: multiple movie directories found error.
        :raises MovieFileNotFoundError: movie file not found error.
        :raises MultipleMovieFilesFoundError: multiple movie files found error.
        :raises StreamDoesNotExistError: stream does not exist error.

        :rtype: bytes
        """

        directory, file = self._transcode(movie_id, **options)
        self.set_access_time(directory)
        return self._send_stream(directory, file)

    def continue_stream(self, movie_id, file, **options):
        """
        continues the streaming of given movie.

        :param uuid.UUID movie_id: movie id to be streamed.
        :param str file: stream file name to be returned.

        :raises StreamDoesNotExistError: stream does not exist error.

        :rtype: bytes
        """

        directory = self._get_stream_path(movie_id)
        self.set_access_time(directory)
        return self._send_stream(directory, file)
