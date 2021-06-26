# -*- coding: utf-8 -*-
"""
directors stats api module.
"""

from pyrin.api.router.decorators import api

import charma.persons.directors.stats.services as director_stat_services


@api('/directors/stats/count', authenticated=False)
def get_count(**options):
    """
    gets total count of directors.

    :rtype: int
    """

    return director_stat_services.get_count()


@api('/directors/stats', authenticated=False)
def get_stats(**options):
    """
    gets different stats of directors.

    :returns: dict(int directors_count: total directors count)
    :rtype: dict
    """

    return director_stat_services.get_stats()
