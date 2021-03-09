# -*- coding: utf-8 -*-
"""
movies related actors services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_persons.actors import RelatedActorsPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(RelatedActorsPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
