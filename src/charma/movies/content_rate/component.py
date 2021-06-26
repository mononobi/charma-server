# -*- coding: utf-8 -*-
"""
movies content rate component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.content_rate import ContentRatePackage
from charma.movies.content_rate.manager import ContentRateManager


@component(ContentRatePackage.COMPONENT_NAME)
class ContentRateComponent(Component, ContentRateManager):
    """
    movies content rate component class.
    """
    pass
