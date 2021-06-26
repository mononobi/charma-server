# -*- coding: utf-8 -*-
"""
media info manager module.
"""

from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager

import pyrin.utils.path as path_utils

from charma.media_info import MediaInfoPackage
from charma.media_info.interface import AbstractMediaInfoProvider
from charma.media_info.exceptions import InvalidMediaInfoProviderTypeError


class MediaInfoManager(Manager, HookMixin):
    """
    media info manager class.
    """

    package_class = MediaInfoPackage
    hook_type = AbstractMediaInfoProvider
    invalid_hook_type_error = InvalidMediaInfoProviderTypeError
    REQUIRED_INFO = ('runtime', 'width', 'height')

    def _is_complete(self, info):
        """
        gets a value indicating that given media info is complete.

        :param dict info: media info to be checked.

        :rtype: bool
        """

        for item in self.REQUIRED_INFO:
            result = info.get(item)
            if result is None or result <= 0:
                return False

        return True

    def register_provider(self, instance):
        """
        registers the given instance into media info providers.

        :param AbstractMediaInfoProvider instance: media info provider instance
                                                   to be registered.

        :raises InvalidMediaInfoProviderTypeError: invalid media info provider type error.
        """

        self.register_hook(instance)

    def get_info(self, file, **options):
        """
        gets a dict containing media info of given file.

        :param str file: absolute path of video file.

        :raises InvalidPathError: invalid path error.
        :raises PathIsNotAbsoluteError: path is not absolute error.
        :raises PathNotExistedError: path not existed error.
        :raises IsNotFileError: is not directory error.

        :returns: dict(int runtime,
                       int width,
                       int height)

        :rtype: dict
        """

        path_utils.assert_is_file(file)
        result = dict()
        for provider in self._get_hooks():
            current_result = provider.get_info(file, **options)
            result.update(current_result)
            if self._is_complete(result) is True:
                break

        result.setdefault('runtime', 0)
        result.setdefault('width', 0)
        result.setdefault('height', 0)
        return result
