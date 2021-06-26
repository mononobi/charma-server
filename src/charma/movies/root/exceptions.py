# -*- coding: utf-8 -*-
"""
movies root exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MovieRootException(CoreException):
    """
    movie root exception.
    """
    pass


class MovieRootBusinessException(CoreBusinessException, MovieRootException):
    """
    movie root business exception.
    """
    pass


class MovieRootPathAlreadyExistedError(MovieRootBusinessException):
    """
    movie root path already existed error.
    """
    pass


class OSTypeIsUnknownError(MovieRootBusinessException):
    """
    os type is unknown error.
    """
    pass
