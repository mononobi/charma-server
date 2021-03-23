# -*- coding: utf-8 -*-
"""
media info manager module.
"""

from os import path

from pyrin.core.globals import _
from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager

from imovie.media_info import MediaInfoPackage
from imovie.media_info.interface import AbstractMediaInfoProvider
from imovie.media_info.exceptions import InvalidMediaInfoProviderTypeError, \
    MediaFileDoesNotExistError, IsNotFileError


class MediaInfoManager(Manager, HookMixin):
    """
    media info manager class.
    """

    package_class = MediaInfoPackage
    hook_type = AbstractMediaInfoProvider
    invalid_hook_type_error = InvalidMediaInfoProviderTypeError
    REQUIRED_INFO = ['runtime', 'width', 'height']

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

    def _validate_file_exists(self, file):
        """
        validates that given file exists.

        :param str file: absolute path of file.

        :raises MediaFileDoesNotExistError: media file does not exist error.
        :raises IsNotFileError: is not file error.
        """

        if not path.exists(file):
            raise MediaFileDoesNotExistError(_('Provided media file path does not exist.'))

        if not path.isfile(file):
            raise IsNotFileError(_('Provided path is not a file.'))

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

        :raises MediaFileDoesNotExistError: media file does not exist error.
        :raises IsNotFileError: is not file error.

        :returns: dict(int runtime,
                       int width,
                       int height)

        :rtype: dict
        """

        self._validate_file_exists(file)
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
