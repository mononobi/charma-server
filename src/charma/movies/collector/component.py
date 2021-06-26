# -*- coding: utf-8 -*-
"""
movies collector component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.collector import MoviesCollectorPackage
from charma.movies.collector.manager import MoviesCollectorManager


@component(MoviesCollectorPackage.COMPONENT_NAME)
class MoviesCollectorComponent(Component, MoviesCollectorManager):
    """
    movies collector component class.
    """
    pass
