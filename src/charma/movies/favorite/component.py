# -*- coding: utf-8 -*-
"""
movies favorite component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.favorite import FavoriteMoviesPackage
from charma.movies.favorite.manager import FavoriteMoviesManager


@component(FavoriteMoviesPackage.COMPONENT_NAME)
class FavoriteMoviesComponent(Component, FavoriteMoviesManager):
    """
    favorite movies component class.
    """
    pass
