# -*- coding: utf-8 -*-
"""
movies manager module.
"""

from pyrin.core.structs import Manager


class MoviesManager(Manager):
    """
    movies manager class.
    """

    def create(self, title, directory_name, **options):
        """
        creates a new movie.

        :param title: movie title.
        :param directory_name: movie directory name.

        :keyword str original_title: movie original title.
        :keyword int production_year: movie production year.
        :keyword float imdb_rate: movie imdb rating.
        :keyword int meta_score: movie meta-critics score.
        :keyword time duration: movie duration.
        :keyword str imdb_page: movie imdb page url.
        :keyword str poster_name: movie poster file name.
        :keyword str storyline: movie storyline.
        :keyword str poster_url: movie poster url.
        :keyword int content_rate: movie mpaa content rating.
        :note content_rate:
            UNKNOWN = 0
            G = 1
            PG = 2
            PG_13 = 3
            R = 4
            NC_17 = 5

        :keyword int resolution: movie resolution.
        :note resolution:
            UNKNOWN = 0
            VCD = 1
            DVD = 2
            HD = 3
            FHD = 4
            UHD = 5

        :returns: created movie id
        :rtype: uuid.UUID
        """
