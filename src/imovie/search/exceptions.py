# -*- coding: utf-8 -*-
"""
search exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class SearchException(CoreException):
    """
    search exception.
    """
    pass


class SearchBusinessException(CoreBusinessException, SearchException):
    """
    search business exception.
    """
    pass


class InvalidSearchProviderTypeError(SearchException):
    """
    invalid search provider type error.
    """
    pass


class DuplicateSearchProviderError(SearchException):
    """
    duplicate search provider error.
    """
    pass


class SearchProviderCategoryNotFoundError(SearchException):
    """
    search provider category not found error.
    """
    pass


class SearchProviderNotFoundError(SearchException):
    """
    search provider not found error.
    """
    pass
