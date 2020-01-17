# -*- coding: utf-8 -*-
"""
movies package.
"""

from pyrin.packaging.context import Package


class MoviesPackage(Package):
    """
    movies package class.
    """

    NAME = __name__
    DEPENDS = []
    COMPONENT_NAME = 'movies.component'
    CONFIG_STORE_NAMES = ['movies']
