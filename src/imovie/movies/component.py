# -*- coding: utf-8 -*-
"""
movies component module.
"""

from pyrin.application.decorators import component
from pyrin.application.context import Component

from imovie.movies import MoviesPackage
from imovie.movies.manager import MoviesManager


@component(MoviesPackage.COMPONENT_NAME)
class MoviesComponent(Component, MoviesManager):
    """
    movies component class.
    """
