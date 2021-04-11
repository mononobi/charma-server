# -*- coding: utf-8 -*-
"""
movies root component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.movies.root import MovieRootPackage
from imovie.movies.root.manager import MovieRootManager


@component(MovieRootPackage.COMPONENT_NAME)
class MovieRootComponent(Component, MovieRootManager):
    """
    movie root component class.
    """
    pass
