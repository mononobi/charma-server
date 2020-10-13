# -*- coding: utf-8 -*-
"""
genres exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class GenresException(CoreException):
    """
    genres exception.
    """
    pass


class GenresBusinessException(CoreBusinessException, GenresException):
    """
    genres business exception.
    """
    pass
