# -*- coding: utf-8 -*-
"""
actors stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.persons.actors.stats import ActorsStatsPackage
from imovie.persons.actors.stats.manager import ActorsStatsManager


@component(ActorsStatsPackage.COMPONENT_NAME)
class ActorsStatsComponent(Component, ActorsStatsManager):
    """
    actors stats component class.
    """
    pass
