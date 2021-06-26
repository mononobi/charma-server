# -*- coding: utf-8 -*-
"""
actors stats package.
"""

from pyrin.packaging.base import Package


class ActorsStatsPackage(Package):
    """
    actors stats package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'persons.actors.stats.component'
    DEPENDS = ['charma.stats']
