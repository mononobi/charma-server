# -*- coding: utf-8 -*-
"""
scraper component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.scraper import ScraperPackage
from imovie.scraper.manager import ScraperManager


@component(ScraperPackage.COMPONENT_NAME)
class ScraperComponent(Component, ScraperManager):
    """
    scraper component class.
    """
    pass
