# -*- coding: utf-8 -*-
"""
updater services module.
"""

from pyrin.application.services import get_component

from imovie.updater import UpdaterPackage


# Usage:
# you could implement different services here and call corresponding manager method this way:
# return get_component(UpdaterPackage.COMPONENT_NAME).method_name(*arg, **kwargs)
