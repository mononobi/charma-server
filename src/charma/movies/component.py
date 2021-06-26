# -*- coding: utf-8 -*-
"""
movies component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies import MoviesPackage
from charma.movies.manager import MoviesManager


@component(MoviesPackage.COMPONENT_NAME)
class MoviesComponent(Component, MoviesManager):
    """
    movies component class.
    """
    pass
