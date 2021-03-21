# -*- coding: utf-8 -*-
"""
movies collector component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.movies.collector import MoviesCollectorPackage
from imovie.movies.collector.manager import MoviesCollectorManager


@component(MoviesCollectorPackage.COMPONENT_NAME)
class MoviesCollectorComponent(Component, MoviesCollectorManager):
    """
    movies collector component class.
    """
    pass
