# -*- coding: utf-8 -*-
"""
movies stats api module.
"""

from pyrin.api.router.decorators import api

import charma.movies.stats.services as movies_stat_services


@api('/movies/stats/average-rate', authenticated=False)
def get_average_rate(**options):
    """
    gets average imdb rate of all movies.

    :rtype: float
    """

    return movies_stat_services.get_average_rate()


@api('/movies/stats/count', authenticated=False)
def get_count(**options):
    """
    gets total count of movies.

    :rtype: int
    """

    return movies_stat_services.get_count()


@api('/movies/stats/highest-rate', authenticated=False)
def get_highest_rate(**options):
    """
    gets the highest imdb rate of movies.

    :rtype: float
    """

    return movies_stat_services.get_highest_rate()


@api('/movies/stats/lowest-rate', authenticated=False)
def get_lowest_rate(**options):
    """
    gets the lowest imdb rate of movies.

    :rtype: float
    """

    return movies_stat_services.get_lowest_rate()


@api('/movies/stats/oldest', authenticated=False)
def get_oldest_production_year(**options):
    """
    gets the oldest production year of movies.

    :rtype: int
    """

    return movies_stat_services.get_oldest_production_year()


@api('/movies/stats/newest', authenticated=False)
def get_newest_production_year(**options):
    """
    gets the newest production year of movies.

    :rtype: int
    """

    return movies_stat_services.get_newest_production_year()


@api('/movies/stats/watched-count', authenticated=False)
def get_watched_movies_count(**options):
    """
    gets total count of watched movies.

    :rtype: int
    """

    return movies_stat_services.get_watched_movies_count()


@api('/movies/stats/runtime', authenticated=False)
def get_total_runtime(**options):
    """
    gets total runtime of all movies in minutes.

    :rtype: int
    """

    return movies_stat_services.get_total_runtime()


@api('/movies/stats/shortest', authenticated=False)
def get_shortest_runtime(**options):
    """
    gets the shortest runtime of movies in minutes.

    :rtype: int
    """

    return movies_stat_services.get_shortest_runtime()


@api('/movies/stats/longest', authenticated=False)
def get_longest_runtime(**options):
    """
    gets the longest runtime of movies in minutes.

    :rtype: int
    """

    return movies_stat_services.get_longest_runtime()


@api('/movies/stats/updated-count', authenticated=False)
def get_updated_movies_count(**options):
    """
    gets total count of updated movies.

    :rtype: int
    """

    return movies_stat_services.get_updated_movies_count()


@api('/movies/stats', authenticated=False)
def get_stats(**options):
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

    return movies_stat_services.get_stats()
