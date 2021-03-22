# -*- coding: utf-8 -*-
"""
media info manager module.
"""

from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager

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
