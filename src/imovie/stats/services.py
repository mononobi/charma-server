# -*- coding: utf-8 -*-
"""
stats services module.
"""

from pyrin.application.services import get_component

from imovie.stats import StatsPackage


def register_hook(instance):
    """
    registers the given instance into stats hooks.

    :param StatsHookBase instance: stats hook instance to be registered.

    :raises InvalidStatsHookTypeError: invalid stats hook type error.
    """

    return get_component(StatsPackage.COMPONENT_NAME).register_hook(instance)


def get_stats(**options):
    """
    gets different stats of application data.

    :rtype: dict
    """

    return get_component(StatsPackage.COMPONENT_NAME).get_stats(**options)
