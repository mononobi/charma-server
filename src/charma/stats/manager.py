# -*- coding: utf-8 -*-
"""
stats manager module.
"""

from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager

from charma.stats import StatsPackage
from charma.stats.hooks import StatsHookBase
from charma.stats.exceptions import InvalidStatsHookTypeError


class StatsManager(Manager, HookMixin):
    """
    stats manager class.
    """

    package_class = StatsPackage
    hook_type = StatsHookBase
    invalid_hook_type_error = InvalidStatsHookTypeError

    def get_stats(self):
        """
        gets different stats of application data.

        :rtype: dict
        """

        result = dict()
        for hook in self._get_hooks():
            stats = hook.get_stats()
            result.update(stats)

        return result
