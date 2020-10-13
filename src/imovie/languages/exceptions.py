# -*- coding: utf-8 -*-
"""
languages exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class LanguagesException(CoreException):
    """
    languages exception.
    """
    pass


class LanguagesBusinessException(CoreBusinessException, LanguagesException):
    """
    languages business exception.
    """
    pass
