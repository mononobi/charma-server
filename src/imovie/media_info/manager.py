# -*- coding: utf-8 -*-
"""
media info manager module.
"""

import pyrin.configuration.services as config_services

from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager

import imovie.utils.path as path_utils

from imovie.media_info import MediaInfoPackage
from imovie.media_info.interface import AbstractMediaInfoProvider
from imovie.media_info.exceptions import InvalidMediaInfoProviderTypeError


class MediaInfoManager(Manager, HookMixin):
    """
    media info manager class.
    """

    package_class = MediaInfoPackage
    hook_type = AbstractMediaInfoProvider
    invalid_hook_type_error = InvalidMediaInfoProviderTypeError

    def __init__(self):
        """
        initializes an instance of MediaInfoManager.
        """

        super().__init__()

        self._video_extensions = self._load_video_extensions()
        self._min_runtime = config_services.get('media.info', 'general', 'min_runtime')
        self._min_size = config_services.get('media.info', 'general', 'min_size')

    def _load_video_extensions(self):
        """
        loads all valid video extensions from config store.

        :rtype: list[str]
        """

        result = config_services.get('media.info', 'general', 'video_extensions')
        return [item.lower() for item in result]

    def _is_complete(self, info):
        """
        gets a value indicating that given media info is complete.

        :param dict info: media info to be checked.

        :rtype: bool
        """

        return 'runtime' in info and 'height' in info and 'width' in info

    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :returns: dict(int runtime,
                       int height,
                       int width)

        :rtype: dict
        """

        result = dict()
        for provider in self._get_hooks():
            current_result = provider.get_info(file, **options)
            result.update(current_result)
            if self._is_complete(result) is True:
                break

        result.setdefault('runtime', 0)
        result.setdefault('height', 0)
        result.setdefault('width', 0)
        return result

    def is_video_extension(self, file, **options):
        """
        gets a value indicating that given file has a valid video file extension.

        :param str file: absolute path of file.

        :rtype: bool
        """

        if file is None:
            return False

        extension = path_utils.get_file_extension(file)
        return extension in self._video_extensions

    def is_video_file(self, file, **options):
        """
        gets a value indicating that given file is a valid video file.

        :param str file: absolute path of file.

        :rtype: bool
        """

        is_extension = self.is_video_extension(file, **options)
        if is_extension is False:
            return False

    def register_provider(self, instance):
        """
        registers the given instance into media info providers.

        :param AbstractMediaInfoProvider instance: media info provider instance
                                                   to be registered.

        :raises InvalidMediaInfoProviderTypeError: invalid media info provider type error.
        """

        self.register_hook(instance)
