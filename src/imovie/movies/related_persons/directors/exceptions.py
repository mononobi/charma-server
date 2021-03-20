# -*- coding: utf-8 -*-
"""
movies related directors exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class RelatedDirectorsException(CoreException):
    """
    movies related directors exception.
    """
    pass


class RelatedDirectorsBusinessException(CoreBusinessException, RelatedDirectorsException):
    """
    movies related directors business exception.
    """
    pass


class Movie2DirectorDoesNotExistError(RelatedDirectorsBusinessException):
    """
    movie 2 director does not exist error.
    """
    pass
