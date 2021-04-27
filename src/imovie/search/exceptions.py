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
