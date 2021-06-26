# -*- coding: utf-8 -*-
"""
movies root component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.root import MovieRootPackage
from charma.movies.root.manager import MovieRootManager


@component(MovieRootPackage.COMPONENT_NAME)
class MovieRootComponent(Component, MovieRootManager):
    """
    movie root component class.
    """
    pass
