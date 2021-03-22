# -*- coding: utf-8 -*-
"""
media info handlers opencv module.
"""

import cv2

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

        video = cv2.VideoCapture(file)
        runtime = self._get_runtime(video)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)

        return dict(runtime=int(runtime), height=int(height), width=int(width))

    def _get_runtime(self, video):
        """
        gets the runtime of given video object in minutes.

        :param VideoCapture video: video object.

        :rtype: int
        """

        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_second = video.get(cv2.CAP_PROP_FPS)
        if frames_per_second == 0:
            return 0

        return (frame_count / frames_per_second) / 60
