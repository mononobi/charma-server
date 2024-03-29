# -*- coding: utf-8 -*-
"""
movies stats component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.movies.stats import MovieStatsPackage
from charma.movies.stats.manager import MovieStatsManager


@component(MovieStatsPackage.COMPONENT_NAME)
class MovieStatsComponent(Component, MovieStatsManager):
    """
    movies stats component class.
    """
    pass
