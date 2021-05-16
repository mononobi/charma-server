# -*- coding: utf-8 -*-
"""
movies stats package.
"""

from pyrin.packaging.base import Package


class MovieStatsPackage(Package):
    """
    movies stats package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'movies.stats.component'
    DEPENDS = ['imovie.stats']
