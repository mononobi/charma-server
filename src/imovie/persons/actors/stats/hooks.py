# -*- coding: utf-8 -*-
"""
actors stats hooks module.
"""

import imovie.persons.actors.stats.services as actor_stat_services

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

        return actor_stat_services.get_stats()
