# -*- coding: utf-8 -*-
"""
movies related genres component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.related_genres import RelatedGenresPackage
from charma.movies.related_genres.manager import RelatedGenresManager


@component(RelatedGenresPackage.COMPONENT_NAME)
class RelatedGenresComponent(Component, RelatedGenresManager):
    """
    movies related genres component class.
    """
    pass
