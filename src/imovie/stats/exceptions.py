# -*- coding: utf-8 -*-
"""
stats exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class StatsException(CoreException):
    """
    stats exception.
    """
    pass


class StatsBusinessException(CoreBusinessException, StatsException):
    """
    stats business exception.
    """
    pass


class InvalidStatsHookTypeError(StatsException):
    """
    invalid stats hook type error.
    """
    pass
