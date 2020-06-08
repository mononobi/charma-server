# -*- coding: utf-8 -*-
"""
movies exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MoviesException(CoreException):
    """
    movies exception.
    """
    pass


class MoviesBusinessException(CoreBusinessException, MoviesException):
    """
    movies business exception.
    """
    pass
