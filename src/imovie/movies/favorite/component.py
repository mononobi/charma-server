# -*- coding: utf-8 -*-
"""
movies favorite component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.movies.favorite import FavoriteMoviesPackage
from imovie.movies.favorite.manager import FavoriteMoviesManager


@component(FavoriteMoviesPackage.COMPONENT_NAME)
class FavoriteMoviesComponent(Component, FavoriteMoviesManager):
    """
    favorite movies component class.
    """
    pass
