# -*- coding: utf-8 -*-
"""
movies related directors hooks module.
"""

import imovie.movies.related_persons.directors.services as related_director_services

from imovie.movies.decorators import movie_hook
from imovie.movies.hooks import MovieHookBase
from imovie.persons.directors.decorators import director_hook
from imovie.persons.directors.hooks import DirectorHookBase


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

        related_director_services.delete_by_movie(id)


@director_hook()
class DirectorHook(DirectorHookBase):
    """
    director hook class.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a director is going to be deleted.

        :param uuid.UUID id: person id.
        """

        related_director_services.delete_by_director(id)
