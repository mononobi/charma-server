# -*- coding: utf-8 -*-
"""
scraper package.
"""

from pyrin.packaging.base import Package


class ScraperPackage(Package):
    """
    scraper package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'scraper.component'
    CONFIG_STORE_NAMES = ['scraper']
