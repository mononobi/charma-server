# -*- coding: utf-8 -*-
"""
streaming interface module.
"""

from threading import Lock
from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError
from pyrin.core.structs import CoreObject, MultiSingletonMeta


class StreamProviderSingletonMeta(MultiSingletonMeta):
    """
    stream provider singleton meta class.

    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractStreamProvider(CoreObject, metaclass=StreamProviderSingletonMeta):
    """
    abstract stream provider class.
    """

    @abstractmethod
    def transcode(self, input_file, output_directory, **options):
        """
        transcodes a video file to output folder.

        :param str input_file: file path to be transcoded.
        :param str output_directory: output directory path.

        :keyword str subtitle: subtitle file path.
        :keyword int threads: number of threads to be used.
        :keyword str preset: transcoding preset name.

        :raises CoreNotImplementedError: core not implemented error.
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def name(self):
        """
        gets the name of this stream provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def output_file(self):
        """
        gets the output file name of this stream provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()
