# -*- coding: utf-8 -*-
"""
streaming providers base module.
"""

import os

from multiprocessing import Process

import ffmpeg

import pyrin.logging.services as logging_services

import imovie.streaming.services as stream_services

from imovie.streaming.enumerations import TranscoderPresetEnum
from imovie.streaming.interface import AbstractStreamProvider


class StreamProviderBase(AbstractStreamProvider):
    """
    stream provider base class.
    """

    LOGGER = logging_services.get_logger('streaming')

    # name of this stream provider.
    _name = None

    # video codec name for transcoding.
    _video_codec = None

    # audio codec name for transcoding.
    _audio_codec = None

    # subtitle codec name for transcoding.
    _subtitle_codec = None

    # default preset name to be used for transcoding.
    _default_preset = TranscoderPresetEnum.FAST

    # stream format name.
    _format = None

    # default threads to be used for transcoding.
    _default_threads = 1

    # output file name.
    _output_file = None

    def _get_transcoding_configs(self):
        """
        gets a dict containing custom transcoding configs.

        this method is intended to be overridden in subclasses.

        :rtype: dict
        """

        return dict()

    def _get_output_path(self, output_directory, **options):
        """
        gets output file name.

        :param str output_directory: output directory path.

        :rtype: str
        """

        return os.path.join(output_directory, self._output_file)

    def _transcode(self, stream, input_file, output_directory, **options):
        """
        transcodes the given stream.

        :param ffmpeg.nodes.OutputStream stream: stream to be transcoded.
        :param str input_file: file path to be transcoded.
        :param str output_directory: output directory path.
        """

        stream_services.set_started(output_directory)
        stream_services.set_access_time(output_directory)
        process = ffmpeg.run_async(stream, overwrite_output=True,
                                   pipe_stderr=True, pipe_stdout=True)
        stream_services.set_process_id(output_directory, process.pid)
        stdout, stderr = process.communicate()
        return_code = process.poll()
        if stdout:
            self.LOGGER.info('Transcoding info for file [{file}]: [{details}]'
                             .format(file=input_file, details=stdout))

        if return_code:
            stream_services.set_failed(output_directory)
            self.LOGGER.error('Transcoding failed for file [{file}]: [{details}]'
                              .format(file=input_file, details=stderr))
        else:
            stream_services.set_finished(output_directory)
            self.LOGGER.info('Transcoding finished for file [{file}].'
                             .format(file=input_file))

    def transcode(self, input_file, output_directory, **options):
        """
        transcodes a video file to output folder.

        :param str input_file: file path to be transcoded.
        :param str output_directory: output directory path.

        :keyword list[str] subtitles: subtitle file paths.
        :keyword int threads: number of threads to be used.
        :keyword str preset: transcoding preset name.
        """

        preset = options.get('preset') or self._default_preset
        threads = options.get('threads') or self._default_threads
        subtitles = options.get('subtitles')

        stream = ffmpeg.input(input_file)
        if subtitles is not None:
            stream = ffmpeg.filter(stream, 'subtitles', subtitles)

        output_path = self._get_output_path(output_directory, **options)
        stream = ffmpeg.output(stream, output_path,
                               loop=0, threads=threads, preset=preset,
                               format=self._format, vcodec=self._video_codec,
                               acodec=self._audio_codec,
                               **self._get_transcoding_configs())

        process = Process(target=self._transcode,
                          args=(stream, input_file, output_directory))
        process.start()

    @property
    def name(self):
        """
        gets the name of this stream provider.

        :rtype: str
        """

        return self._name

    @property
    def output_file(self):
        """
        gets the output file name of this stream provider.

        :rtype: str
        """

        return self._output_file
