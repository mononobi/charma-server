# -*- coding: utf-8 -*-
"""
directors services module.
"""

from pyrin.application.services import get_component

from imovie.persons.directors import DirectorsPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(DirectorsPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
