# -*- coding: utf-8 -*-
"""
actors handler module.
"""

import charma.persons.actors.services as actor_services

from charma.persons.decorators import person_handler
from charma.persons.enumerations import PersonTypeEnum
from charma.persons.handler import AbstractPersonHandler


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
