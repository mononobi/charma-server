# -*- coding: utf-8 -*-
"""
movies collector manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.movies.collector import MoviesCollectorPackage


class MoviesCollectorManager(Manager):
    """
    movies collector manager class.
    """

    package_class = MoviesCollectorPackage
