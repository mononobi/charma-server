# -*- coding: utf-8 -*-
"""
movies related directors component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.related_persons.directors import RelatedDirectorsPackage
from charma.movies.related_persons.directors.manager import RelatedDirectorsManager


@component(RelatedDirectorsPackage.COMPONENT_NAME)
class RelatedDirectorsComponent(Component, RelatedDirectorsManager):
    """
    movies related directors component class.
    """
    pass
