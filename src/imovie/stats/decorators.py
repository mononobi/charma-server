# -*- coding: utf-8 -*-
"""
stats decorators module.
"""

import imovie.stats.services as stat_services


def stats_hook():
    """
    decorator to register a stats hook.

    :raises InvalidStatsHookTypeError: invalid stats hook type error.

    :returns: stats hook class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available stats hooks.

        :param type cls: stats hook class.

        :returns: stats hook class.
        :rtype: type
        """

        instance = cls()
        stat_services.register_hook(instance)

        return cls

    return decorator
