# -*- coding: utf-8 -*-
"""
media info handlers base module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

from imovie.media_info.interface import AbstractMediaInfoProvider


class MediaInfoProviderBase(AbstractMediaInfoProvider):
    """
    media info provider base class.
    """

    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """

        result = self._get_info(file, **options)
        runtime = result.get('runtime')
        height = result.get('height')
        width = result.get('width')

        if runtime is None or runtime <= 0:
            result.pop('runtime', None)

        if height is None or height <= 0:
            result.pop('height', None)

        if width is None or width <= 0:
            result.pop('width', None)

        return result

    @abstractmethod
    def _get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        subclasses must override this method.

        :param str file: absolute path of video file.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """

        raise CoreNotImplementedError()
