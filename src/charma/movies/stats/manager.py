# -*- coding: utf-8 -*-
"""
movies stats manager module.
"""

from sqlalchemy import func

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from charma.movies.models import MovieEntity
from charma.movies.stats import MovieStatsPackage


class MovieStatsManager(Manager):
    """
    movies stats manager class.
    """

    package_class = MovieStatsPackage

    def get_average_rate(self):
        """
        gets average imdb rate of all movies.

        :rtype: float
        """

        store = get_current_store()
        result = store.query(func.avg(MovieEntity.imdb_rate))\
            .filter(MovieEntity.imdb_rate != None).scalar()

        if result is not None:
            return round(result, 1)

        return result

    def get_count(self):
        """
        gets total count of movies.

        :rtype: int
        """

        store = get_current_store()
        return store.query(MovieEntity.id).count()

    def get_highest_rate(self):
        """
        gets the highest imdb rate of movies.

        :rtype: float
        """

        store = get_current_store()
        return store.query(func.max(MovieEntity.imdb_rate))\
            .filter(MovieEntity.imdb_rate != None).scalar()

    def get_lowest_rate(self):
        """
        gets the lowest imdb rate of movies.

        :rtype: float
        """

        store = get_current_store()
        return store.query(func.min(MovieEntity.imdb_rate))\
            .filter(MovieEntity.imdb_rate != None).scalar()

    def get_oldest_production_year(self):
        """
        gets the oldest production year of movies.

        :rtype: int
        """

        store = get_current_store()
        return store.query(func.min(MovieEntity.production_year))\
            .filter(MovieEntity.production_year != None).scalar()

    def get_newest_production_year(self):
        """
        gets the newest production year of movies.

        :rtype: int
        """

        store = get_current_store()
        return store.query(func.max(MovieEntity.production_year))\
            .filter(MovieEntity.production_year != None).scalar()

    def get_watched_movies_count(self):
        """
        gets total count of watched movies.

        :rtype: int
        """

        store = get_current_store()
        return store.query(MovieEntity.id).filter(MovieEntity.is_watched == True).count()

    def get_total_runtime(self):
        """
        gets total runtime of all movies in minutes.

        :rtype: int
        """

        store = get_current_store()
        return store.query(func.sum(MovieEntity.runtime))\
            .filter(MovieEntity.runtime != None).scalar()

    def get_shortest_runtime(self):
        """
        gets the shortest runtime of movies in minutes.

        :rtype: int
        """

        store = get_current_store()
        return store.query(func.min(MovieEntity.runtime))\
            .filter(MovieEntity.runtime != None).scalar()

    def get_longest_runtime(self):
        """
        gets the longest runtime of movies in minutes.

        :rtype: int
        """

        store = get_current_store()
        return store.query(func.max(MovieEntity.runtime))\
            .filter(MovieEntity.runtime != None).scalar()

    def get_updated_movies_count(self):
        """
        gets total count of updated movies.

        :rtype: int
        """

        store = get_current_store()
        return store.query(MovieEntity.id).filter(MovieEntity.modified_on != None).count()

    def get_stats(self):
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

        count = self.get_count()
        average_rate = self.get_average_rate()
        highest_rate = self.get_highest_rate()
        lowest_rate = self.get_lowest_rate()
        oldest_movie = self.get_oldest_production_year()
        newest_movie = self.get_newest_production_year()
        watched_movies = self.get_watched_movies_count()
        total_runtime = self.get_total_runtime()
        shortest_runtime = self.get_shortest_runtime()
        longest_runtime = self.get_longest_runtime()
        updated_movies = self.get_updated_movies_count()

        return dict(movies_count=count,
                    average_rate=average_rate,
                    highest_rate=highest_rate,
                    lowest_rate=lowest_rate,
                    oldest_movie=oldest_movie,
                    newest_movie=newest_movie,
                    watched_movies=watched_movies,
                    total_runtime=total_runtime,
                    shortest_runtime=shortest_runtime,
                    longest_runtime=longest_runtime,
                    updated_movies=updated_movies)
