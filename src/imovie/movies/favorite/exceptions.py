# -*- coding: utf-8 -*-
"""
movies favorite exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class FavoriteMoviesException(CoreException):
    """
    favorite movies exception.
    """
    pass


class FavoriteMoviesBusinessException(CoreBusinessException, FavoriteMoviesException):
    """
    favorite movies business exception.
    """
    pass


class FavoriteMovieDoesNotExistError(FavoriteMoviesBusinessException):
    """
    favorite movie does not exist error.
    """
    pass
