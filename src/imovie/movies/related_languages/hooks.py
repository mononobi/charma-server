# -*- coding: utf-8 -*-
"""
movies related languages hooks module.
"""

import imovie.movies.related_languages.services as related_language_services

from imovie.movies.decorators import movie_hook
from imovie.movies.hooks import MovieHookBase


@movie_hook()
class MovieHook(MovieHookBase):
    """
    movie hook class.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a movie is going to be deleted.

        :param uuid.UUID id: movie id.
        """

        related_language_services.delete_by_movie(id)