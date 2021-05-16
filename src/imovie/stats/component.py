# -*- coding: utf-8 -*-
"""
stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.stats import StatsPackage
from imovie.stats.manager import StatsManager


@component(StatsPackage.COMPONENT_NAME)
class StatsComponent(Component, StatsManager):
    """
    stats component class.
    """
    pass
