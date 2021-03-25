# -*- coding: utf-8 -*-
"""
movies collector exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MoviesCollectorException(CoreException):
    """
    movies collector exception.
    """
    pass


class MoviesCollectorBusinessException(CoreBusinessException, MoviesCollectorException):
    """
    movies collector business exception.
    """
    pass


class DirectoryIsIgnoredError(MoviesCollectorBusinessException):
    """
    directory is ignored error.
    """
    pass


class MovieIsAlreadyCollectedError(MoviesCollectorBusinessException):
    """
    movie is already collected error.
    """
    pass


class DirectoryIsEmptyError(MoviesCollectorBusinessException):
    """
    directory is empty error.
    """
    pass
