# -*- coding: utf-8 -*-
"""
movies related actors exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class RelatedActorsException(CoreException):
    """
    movies related actors exception.
    """
    pass


class RelatedActorsBusinessException(CoreBusinessException, RelatedActorsException):
    """
    movies related actors business exception.
    """
    pass


class Movie2ActorDoesNotExistError(RelatedActorsBusinessException):
    """
    movie 2 actor does not exist error.
    """
    pass
