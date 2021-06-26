# -*- coding: utf-8 -*-
"""
media info handlers base module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

from charma.media_info.interface import AbstractMediaInfoProvider


class MediaInfoProviderBase(AbstractMediaInfoProvider):
    """
    media info provider base class.
    """

    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :returns: dict(int runtime,
                       int width,
                       int height)

        :rtype: dict
        """

        video = self._get_video_object(file, **options)
        runtime = self._get_runtime(video, **options)
        width, height = self._get_resolution(video, **options)
        result = dict()

        if runtime is not None and runtime > 0:
            result.update(runtime=int(runtime))

        if width is not None and width > 0:
            result.update(width=int(width))

        if height is not None and height > 0:
            result.update(height=int(height))

        return result

    @abstractmethod
    def _get_video_object(self, file, **options):
        """
        gets the video object from given file.

        this method must be overridden in subclasses.

        :param str file: absolute path of video file.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: object
        """

        raise CoreNotImplementedError()

    @abstractmethod
    def _get_runtime(self, video, **options):
        """
        gets the runtime from given video object in minutes.

        this method must be overridden in subclasses.

        :param object video: video object.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: int
        """

        raise CoreNotImplementedError()

    @abstractmethod
    def _get_resolution(self, video, **options):
        """
        gets the resolution of given video object.

        it must return a tuple of two items. first item is width, the second is height.
        this method must be overridden in subclasses.

        :param object video: video object.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: tuple[int width, int height]
        :rtype: tuple[int, int]
        """

        raise CoreNotImplementedError()
