# -*- coding: utf-8 -*-
"""
movies favorite hooks module.
"""

import charma.movies.favorite.services as favorite_movie_services

from charma.movies.decorators import movie_hook
from charma.movies.hooks import MovieHookBase


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

        favorite_movie_services.delete(id)
