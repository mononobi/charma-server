# -*- coding: utf-8 -*-
"""
movies images exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MoviesImagesException(CoreException):
    """
    movies images exception.
    """
    pass


class MoviesImagesBusinessException(CoreBusinessException, MoviesImagesException):
    """
    movies images business exception.
    """
    pass
