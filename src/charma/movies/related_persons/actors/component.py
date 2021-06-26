# -*- coding: utf-8 -*-
"""
movies related actors component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.related_persons.actors import RelatedActorsPackage
from charma.movies.related_persons.actors.manager import RelatedActorsManager


@component(RelatedActorsPackage.COMPONENT_NAME)
class RelatedActorsComponent(Component, RelatedActorsManager):
    """
    movies related actors component class.
    """
    pass
