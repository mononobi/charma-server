# -*- coding: utf-8 -*-
"""
movies stats exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MovieStatsException(CoreException):
    """
    movies stats exception.
    """
    pass


class MovieStatsBusinessException(CoreBusinessException, MovieStatsException):
    """
    movies stats business exception.
    """
    pass
