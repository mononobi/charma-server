# -*- coding: utf-8 -*-
"""
directors stats services module.
"""

from pyrin.application.services import get_component

from imovie.persons.directors.stats import DirectorsStatsPackage


def get_count():
    """
    gets total count of directors.

    :rtype: int
    """

    return get_component(DirectorsStatsPackage.COMPONENT_NAME).get_count()


def get_stats():
    """
    gets different stats of directors.

    :returns: dict(int directors_count: total directors count)
    :rtype: dict
    """

    return get_component(DirectorsStatsPackage.COMPONENT_NAME).get_stats()
