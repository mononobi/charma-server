# -*- coding: utf-8 -*-
"""
movies related actors hooks module.
"""

import imovie.movies.related_persons.actors.services as related_actors_services

from imovie.movies.decorators import movie_hook
from imovie.movies.hooks import MovieHookBase
from imovie.persons.decorators import person_hook
from imovie.persons.hooks import PersonHookBase


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

        related_actors_services.delete_by_movie(id)


@person_hook()
class PersonHook(PersonHookBase):
    """
    person hook class.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a person is going to be deleted.

        :param uuid.UUID id: person id.
        """

        related_actors_services.delete_by_person(id)
