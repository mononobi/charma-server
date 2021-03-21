# -*- coding: utf-8 -*-
"""
movies related genres exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class RelatedGenresException(CoreException):
    """
    movies related_genres exception.
    """
    pass


class RelatedGenresBusinessException(CoreBusinessException, RelatedGenresException):
    """
    movies related_genres business exception.
    """
    pass


class Movie2GenreDoesNotExistError(RelatedGenresBusinessException):
    """
    movie 2 genre does not exist error.
    """
    pass
