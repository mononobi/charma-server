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


class MovieDoesNotExistError(MoviesBusinessException):
    """
    movie does not exist error.
    """
    pass


class InvalidMovieHookTypeError(MoviesException):
    """
    invalid movie hook type error.
    """
    pass
