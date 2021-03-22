# -*- coding: utf-8 -*-
"""
media info handlers base module.
"""

from os import path
from abc import abstractmethod

from pyrin.core.globals import _
from pyrin.core.exceptions import CoreNotImplementedError

from imovie.media_info.interface import AbstractMediaInfoProvider
from imovie.media_info.handlers.exceptions import MediaFileDoesNotExistError, \
    InvalidMediaFileError


class MediaInfoProviderBase(AbstractMediaInfoProvider):
    """
    media info provider base class.
    """

    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :raises MediaFileDoesNotExistError: media file does not exist error.
        :raises InvalidMediaFileError: invalid media file error.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """

        if not path.exists(file):
            raise MediaFileDoesNotExistError(_('Provided media file path does not exist.'))

        if not path.isfile(file):
            raise InvalidMediaFileError(_('Provided path is not a file.'))

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
