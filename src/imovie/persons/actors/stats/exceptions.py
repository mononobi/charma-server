# -*- coding: utf-8 -*-
"""
actors stats exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ActorsStatsException(CoreException):
    """
    actors stats exception.
    """
    pass


class ActorsStatsBusinessException(CoreBusinessException, ActorsStatsException):
    """
    actors stats business exception.
    """
    pass
