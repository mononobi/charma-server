# -*- coding: utf-8 -*-
"""
movies related languages exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class RelatedLanguagesException(CoreException):
    """
    movies related languages exception.
    """
    pass


class RelatedLanguagesBusinessException(CoreBusinessException, RelatedLanguagesException):
    """
    movies related languages business exception.
    """
    pass


class Movie2LanguageDoesNotExistError(RelatedLanguagesBusinessException):
    """
    movie 2 language does not exist error.
    """
    pass
