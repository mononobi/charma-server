# -*- coding: utf-8 -*-
"""
actors hooks module.
"""

from pyrin.core.structs import Hook

import charma.persons.actors.services as actor_services

from charma.persons.decorators import person_hook
from charma.persons.hooks import PersonHookBase


class ActorHookBase(Hook):
    """
    actor hook base class.

    all packages that need to be hooked in actors business, must implement
    this class and register an instance of it in actor hooks.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever an actor is going to be deleted.

        :param uuid.UUID id: person id.
        """
        pass


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

        actor_services.delete(id)
