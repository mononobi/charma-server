# -*- coding: utf-8 -*-
"""
actors services module.
"""

from pyrin.application.services import get_component

from imovie.persons.actors import ActorsPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(ActorsPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
