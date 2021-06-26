# -*- coding: utf-8 -*-
"""
movies favorite package.
"""

from pyrin.packaging.base import Package


class FavoriteMoviesPackage(Package):
    """
    favorite movies package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'movies.favorite.component'
