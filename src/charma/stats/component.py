# -*- coding: utf-8 -*-
"""
stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.stats import StatsPackage
from charma.stats.manager import StatsManager


@component(StatsPackage.COMPONENT_NAME)
class StatsComponent(Component, StatsManager):
    """
    stats component class.
    """
    pass
