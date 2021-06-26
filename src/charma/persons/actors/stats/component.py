# -*- coding: utf-8 -*-
"""
actors stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.persons.actors.stats import ActorsStatsPackage
from charma.persons.actors.stats.manager import ActorsStatsManager


@component(ActorsStatsPackage.COMPONENT_NAME)
class ActorsStatsComponent(Component, ActorsStatsManager):
    """
    actors stats component class.
    """
    pass
