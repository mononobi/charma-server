# -*- coding: utf-8 -*-
"""
movies images hooks module.
"""

import imovie.movies.images.services as movie_image_services

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

        movie_image_services.delete(id)
