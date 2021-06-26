# -*- coding: utf-8 -*-
"""
movies related countries component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.related_countries import RelatedCountriesPackage
from charma.movies.related_countries.manager import RelatedCountriesManager


@component(RelatedCountriesPackage.COMPONENT_NAME)
class RelatedCountriesComponent(Component, RelatedCountriesManager):
    """
    movies related countries component class.
    """
    pass
