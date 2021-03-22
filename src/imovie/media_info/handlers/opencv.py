# -*- coding: utf-8 -*-
"""
media info handlers opencv module.
"""

from imovie.media_info.handlers.base import MediaInfoProviderBase


class OpenCVMediaInfoProvider(MediaInfoProviderBase):
    """
    opencv media info provider class.
    """

    def _get_info(self, file):
        """
        gets a dict containing media info of given file.

        it returns None if it could not detect media info.

        :param str file: absolute path of video file.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """
        pass
