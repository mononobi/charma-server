# -*- coding: utf-8 -*-
"""
media info handlers opencv module.
"""

from imovie.media_info.decorators import media_info_provider
from imovie.media_info.handlers.base import MediaInfoProviderBase


@media_info_provider()
class OpenCVMediaInfoProvider(MediaInfoProviderBase):
    """
    opencv media info provider class.
    """

    def _get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """
        pass
