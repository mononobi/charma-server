# -*- coding: utf-8 -*-
"""
search component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.search import SearchPackage
from imovie.search.manager import SearchManager


@component(SearchPackage.COMPONENT_NAME)
class SearchComponent(Component, SearchManager):
    """
    search component class.
    """
    pass
