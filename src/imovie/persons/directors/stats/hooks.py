# -*- coding: utf-8 -*-
"""
directors stats hooks module.
"""

import imovie.persons.directors.stats.services as director_stat_services

from imovie.stats.decorators import stats_hook
from imovie.stats.hooks import StatsHookBase


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

        return director_stat_services.get_stats()
