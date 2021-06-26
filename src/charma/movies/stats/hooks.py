# -*- coding: utf-8 -*-
"""
movies stats hooks module.
"""

import charma.movies.stats.services as movie_stat_services

from charma.stats.decorators import stats_hook
from charma.stats.hooks import StatsHookBase


@stats_hook()
class StatsHook(StatsHookBase):
    """
    stats hook class.
    """

    def get_stats(self):
        """
        this method will be get called whenever stats are requested.

        :rtype: dict
        """

        return movie_stat_services.get_stats()
