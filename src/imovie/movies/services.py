# -*- coding: utf-8 -*-
"""
movies services module.
"""

from pyrin.application.services import get_component

from imovie.movies import MoviesPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(MoviesPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
