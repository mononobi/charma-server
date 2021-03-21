# -*- coding: utf-8 -*-
"""
movies collector services module.
"""

from pyrin.application.services import get_component

from imovie.movies.collector import MoviesCollectorPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(MoviesCollectorPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
