# -*- coding: utf-8 -*-
"""
directors stats exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class DirectorsStatsException(CoreException):
    """
    directors stats exception.
    """
    pass


class DirectorsStatsBusinessException(CoreBusinessException, DirectorsStatsException):
    """
    directors stats business exception.
    """
    pass
