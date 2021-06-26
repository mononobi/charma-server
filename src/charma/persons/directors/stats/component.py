# -*- coding: utf-8 -*-
"""
directors stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.persons.directors.stats import DirectorsStatsPackage
from charma.persons.directors.stats.manager import DirectorsStatsManager


@component(DirectorsStatsPackage.COMPONENT_NAME)
class DirectorsStatsComponent(Component, DirectorsStatsManager):
    """
    directors stats component class.
    """
    pass
