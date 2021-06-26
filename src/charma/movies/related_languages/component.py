# -*- coding: utf-8 -*-
"""
movies related languages component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.related_languages import RelatedLanguagesPackage
from charma.movies.related_languages.manager import RelatedLanguagesManager


@component(RelatedLanguagesPackage.COMPONENT_NAME)
class RelatedLanguagesComponent(Component, RelatedLanguagesManager):
    """
    movies related languages component class.
    """
    pass
