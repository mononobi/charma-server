# -*- coding: utf-8 -*-
"""
media info services module.
"""

from pyrin.application.services import get_component

from imovie.media_info import MediaInfoPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(MediaInfoPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
