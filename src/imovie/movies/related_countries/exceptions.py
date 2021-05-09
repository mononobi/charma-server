# -*- coding: utf-8 -*-
"""
movies related countries exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class RelatedCountriesException(CoreException):
    """
    movies related countries exception.
    """
    pass


class RelatedCountriesBusinessException(CoreBusinessException, RelatedCountriesException):
    """
    movies related countries business exception.
    """
    pass


class Movie2CountryDoesNotExistError(RelatedCountriesBusinessException):
    """
    movie 2 country does not exist error.
    """
    pass
