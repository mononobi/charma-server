# -*- coding: utf-8 -*-
"""
search component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.search import SearchPackage
from charma.search.manager import SearchManager


@component(SearchPackage.COMPONENT_NAME)
class SearchComponent(Component, SearchManager):
    """
    search component class.
    """
    pass
