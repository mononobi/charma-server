# -*- coding: utf-8 -*-
"""
genres component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.genres import GenresPackage
from imovie.genres.manager import GenresManager


@component(GenresPackage.COMPONENT_NAME)
class GenresComponent(Component, GenresManager):
    """
    genres component class.
    """
    pass
