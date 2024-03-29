# -*- coding: utf-8 -*-
"""
media info exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MediaInfoException(CoreException):
    """
    media info exception.
    """
    pass


class MediaInfoBusinessException(CoreBusinessException, MediaInfoException):
    """
    media info business exception.
    """
    pass


class InvalidMediaInfoProviderTypeError(MediaInfoException):
    """
    invalid media info provider type error.
    """
    pass
