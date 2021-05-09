# -*- coding: utf-8 -*-
"""
countries exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class CountriesException(CoreException):
    """
    countries exception.
    """
    pass


class CountriesBusinessException(CoreBusinessException, CountriesException):
    """
    countries business exception.
    """
    pass


class CountryDoesNotExistError(CountriesBusinessException):
    """
    country does not exist error.
    """
    pass
