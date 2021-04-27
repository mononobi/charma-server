# -*- coding: utf-8 -*-
"""
search services module.
"""

from pyrin.application.services import get_component

from imovie.search import SearchPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(SearchPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
