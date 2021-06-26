# -*- coding: utf-8 -*-
"""
genres component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.genres import GenresPackage
from charma.genres.manager import GenresManager


@component(GenresPackage.COMPONENT_NAME)
class GenresComponent(Component, GenresManager):
    """
    genres component class.
    """
    pass
