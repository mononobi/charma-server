# -*- coding: utf-8 -*-
"""
updater processors genre module.
"""

import imovie.genres.services as genre_services
import imovie.movies.related_genres.services as related_genre_services

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class GenreProcessor(ProcessorBase):
    """
    genre processor class.
    """

    _category = UpdaterCategoryEnum.GENRE

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param list[str] data: list of genres to be processed.
        """

        related_genre_services.delete_by_movie(movie_id, **options)
        genres = []
        for item in data:
            genre = genre_services.get_by_name(item)
            genre_id = None
            if genre is not None:
                genre_id = genre.id
            else:
                genre_id = genre_services.create(item, **options)

            genres.append(genre_id)

        for index, item in enumerate(genres):
            is_main = index == 0
            related_genre_services.create(movie_id, item, is_main=is_main)
