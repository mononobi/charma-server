# -*- coding: utf-8 -*-
"""
media info interface module.
"""

from threading import Lock
from abc import abstractmethod

from pyrin.core.structs import CoreObject, MultiSingletonMeta
from pyrin.core.exceptions import CoreNotImplementedError


class MediaInfoSingletonMeta(MultiSingletonMeta):
    """
    media info singleton meta class.

    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractMediaInfoProvider(CoreObject, metaclass=MediaInfoSingletonMeta):
    """
    abstract media info provider class.
    """

    @abstractmethod
    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """

        raise CoreNotImplementedError()
