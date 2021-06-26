# -*- coding: utf-8 -*-
"""
movies images component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.images import MoviesImagesPackage
from charma.movies.images.manager import MoviesImagesManager


@component(MoviesImagesPackage.COMPONENT_NAME)
class MoviesImagesComponent(Component, MoviesImagesManager):
    """
    movies images component class.
    """
    pass
