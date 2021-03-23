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

    def _get_video_object(self, file, **options):
        """
        gets the video object from given file.

        :param str file: absolute path of video file.

        :rtype: cv2.VideoCapture
        """

        return cv2.VideoCapture(file)

    def _get_runtime(self, video, **options):
        """
        gets the runtime from given video object in minutes.

        :param cv2.VideoCapture video: video object.

        :rtype: int
        """

        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_second = video.get(cv2.CAP_PROP_FPS)
        if frames_per_second == 0:
            return 0

        return int((frame_count / frames_per_second) / 60)

    def _get_resolution(self, video, **options):
        """
        gets the resolution of given video object.

        it returns a tuple of two items. first item is width, the second is height.

        :param cv2.VideoCapture video: video object.

        :returns: tuple[int width, int height]
        :rtype: tuple[int, int]
        """

        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

        return int(width), int(height)
