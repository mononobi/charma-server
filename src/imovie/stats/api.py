# -*- coding: utf-8 -*-
"""
stats api module.
"""

from pyrin.api.router.decorators import api

import imovie.stats.services as stats_services


@api('/stats', authenticated=False)
def get_stats(**options):
    """
    gets different stats of application data.

    :rtype: dict
    """

    return stats_services.get_stats(**options)
