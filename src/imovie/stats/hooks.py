# -*- coding: utf-8 -*-
"""
stats hooks module.
"""

from pyrin.core.structs import Hook


class StatsHookBase(Hook):
    """
    stats hook base class.

    all packages that need to be hooked in stats business, must implement
    this class and register an instance of it in stats hooks.
    """

    def get_stats(self, **options):
        """
        this method will be get called whenever stats are requested.

        :rtype: dict
        """

        return dict()
