# -*- coding: utf-8 -*-
"""
actors stats api module.
"""

from pyrin.api.router.decorators import api

import imovie.persons.actors.stats.services as actor_stat_services


@api('/actors/stats/count', authenticated=False)
def get_count(**options):
    """
    gets total count of actors.

    :rtype: int
    """

    return actor_stat_services.get_count()


@api('/actors/stats', authenticated=False)
def get_stats(**options):
    """
    gets different stats of actors.

    :returns: dict(int actors_count: total actors count)
    :rtype: dict
    """

    return actor_stat_services.get_stats()
