# -*- coding: utf-8 -*-
"""
movies related directors services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_persons.directors import RelatedDirectorsPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(RelatedDirectorsPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
