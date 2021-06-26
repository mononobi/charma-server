# -*- coding: utf-8 -*-
"""
actors stats services module.
"""

from pyrin.application.services import get_component

from charma.persons.actors.stats import ActorsStatsPackage


def get_count():
    """
    gets total count of actors.

    :rtype: int
    """

    return get_component(ActorsStatsPackage.COMPONENT_NAME).get_count()


def get_stats():
    """
    gets different stats of actors.

    :returns: dict(int actors_count: total actors count)
    :rtype: dict
    """

    return get_component(ActorsStatsPackage.COMPONENT_NAME).get_stats()
