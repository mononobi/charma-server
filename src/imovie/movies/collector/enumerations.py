# -*- coding: utf-8 -*-
"""
movies collector enumerations module.
"""

from pyrin.core.enumerations import CoreEnum


class CollectResultEnum(CoreEnum):
    """
    collect result enum.
    """

    UNKNOWN = 0
    EMPTY_FOLDER = 1
    ALREADY_EXISTED = 2
    IGNORED = 3
    COLLECTED = 4
