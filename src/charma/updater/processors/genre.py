# -*- coding: utf-8 -*-
"""
updater processors genre module.
"""

import charma.genres.services as genre_services
import charma.movies.related_genres.services as related_genre_services

from charma.updater.decorators import processor
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.processors.base import ProcessorBase


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

        :keyword str imdb_page: movie imdb page.
        """

        related_genre_services.delete_by_movie(movie_id, **options)
        for index, item in enumerate(data):
            is_main = index == 0
            genre = genre_services.get_by_name(item)
            genre_id = None
            if genre is not None:
                genre_id = genre.id
            else:
                genre_id = genre_services.create(item, **options)

            related_genre_services.create(movie_id, genre_id, is_main=is_main)
