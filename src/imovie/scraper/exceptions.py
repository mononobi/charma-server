# -*- coding: utf-8 -*-
"""
scraper exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ScraperException(CoreException):
    """
    scraper exception.
    """
    pass


class ScraperBusinessException(CoreBusinessException, ScraperException):
    """
    scraper business exception.
    """
    pass
