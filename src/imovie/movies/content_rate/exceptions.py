# -*- coding: utf-8 -*-
"""
movies content rate exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ContentRateException(CoreException):
    """
    movies content rate exception.
    """
    pass


class ContentRateBusinessException(CoreBusinessException, ContentRateException):
    """
    movies content rate business exception.
    """
    pass


class ContentRateDoesNotExistError(ContentRateBusinessException):
    """
    content rate does not exist error.
    """
    pass
