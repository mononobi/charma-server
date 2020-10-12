# -*- coding: utf-8 -*-
"""
persons services module.
"""

from pyrin.application.services import get_component

from imovie.persons import PersonsPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(PersonsPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
