# -*- coding: utf-8 -*-
"""
actors handler module.
"""

import imovie.persons.actors.services as actor_services

from imovie.persons.decorators import person_handler
from imovie.persons.enumerations import PersonTypeEnum
from imovie.persons.handler import AbstractPersonHandler


@person_handler()
class ActorHandler(AbstractPersonHandler):
    """
    actor handler class.
    """

    name = PersonTypeEnum.ACTOR

    def create(self, id, **options):
        """
        creates an actor with given inputs.

        :param uuid.UUID id: person id.
        """

        actor_services.create(id, **options)
