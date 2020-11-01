# -*- coding: utf-8 -*-
"""
actors handler module.
"""

import imovie.persons.actors.services as actors_services

from imovie.persons.decorators import person_handler
from imovie.persons.handler import AbstractPersonHandler


@person_handler()
class ActorHandler(AbstractPersonHandler):
    """
    actor handler class.
    """

    name = 'actor'

    def create(self, id, **options):
        """
        creates an actor with given inputs.

        :param int id: person id.
        """

        actors_services.create(id, **options)

    def delete(self, id, **options):
        """
        deletes the given actor.

        :param int id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        actors_services.delete(id)
