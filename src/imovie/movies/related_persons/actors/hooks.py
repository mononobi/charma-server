# -*- coding: utf-8 -*-
"""
movies related actors hooks module.
"""

import imovie.movies.related_persons.actors.services as related_actor_services

from imovie.movies.decorators import movie_hook
from imovie.movies.hooks import MovieHookBase
from imovie.persons.actors.decorators import actor_hook
from imovie.persons.actors.hooks import ActorHookBase


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

        related_actor_services.delete_by_movie(id)


@actor_hook()
class ActorHook(ActorHookBase):
    """
    actor hook class.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever an actor is going to be deleted.

        :param uuid.UUID id: person id.
        """

        related_actor_services.delete_by_actor(id)
