# -*- coding: utf-8 -*-
"""
directors stats package.
"""

from pyrin.packaging.base import Package


class DirectorsStatsPackage(Package):
    """
    directors stats package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'persons.directors.stats.component'
    DEPENDS = ['imovie.stats']
