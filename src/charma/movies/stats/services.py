# -*- coding: utf-8 -*-
"""
movies stats services module.
"""

from pyrin.application.services import get_component

from charma.movies.stats import MovieStatsPackage


def get_average_rate():
    """
    gets average imdb rate of all movies.

    :rtype: float
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_average_rate()


def get_count():
    """
    gets total count of movies.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_count()


def get_highest_rate():
    """
    gets the highest imdb rate of movies.

    :rtype: float
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_highest_rate()


def get_lowest_rate():
    """
    gets the lowest imdb rate of movies.

    :rtype: float
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_lowest_rate()


def get_oldest_production_year():
    """
    gets the oldest production year of movies.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_oldest_production_year()


def get_newest_production_year():
    """
    gets the newest production year of movies.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_newest_production_year()


def get_watched_movies_count():
    """
    gets total count of watched movies.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_watched_movies_count()


def get_total_runtime():
    """
    gets total runtime of all movies in minutes.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_total_runtime()


def get_shortest_runtime():
    """
    gets the shortest runtime of movies in minutes.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_shortest_runtime()


def get_longest_runtime():
    """
    gets the longest runtime of movies in minutes.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_longest_runtime()


def get_updated_movies_count():
    """
    gets total count of updated movies.

    :rtype: int
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_updated_movies_count()


def get_stats():
    """
    gets different stats of movies.

    :returns: dict(int movies_count: total movies count,
                   float average_rate: average imdb rate,
                   float highest_rate: highest imdb rate,
                   float lowest_rate: lowest imdb rate,
                   int oldest_movie: oldest movie production year,
                   int newest_movie: newest movie production year,
                   int watched_movies: watched movies count,
                   int total_runtime: total movies runtime,
                   int shortest_runtime: shortest movie runtime,
                   int longest_runtime: longest movie runtime,
                   int updated_movies: updated movies count)
    :rtype: dict
    """

    return get_component(MovieStatsPackage.COMPONENT_NAME).get_stats()
