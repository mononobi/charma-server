# -*- coding: utf-8 -*-
"""
scraper component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.scraper import ScraperPackage
from charma.scraper.manager import ScraperManager


@component(ScraperPackage.COMPONENT_NAME)
class ScraperComponent(Component, ScraperManager):
    """
    scraper component class.
    """
    pass
