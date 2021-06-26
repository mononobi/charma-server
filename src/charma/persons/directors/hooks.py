# -*- coding: utf-8 -*-
"""
directors hooks module.
"""

from pyrin.core.structs import Hook

import charma.persons.directors.services as director_services

from charma.persons.decorators import person_hook
from charma.persons.hooks import PersonHookBase


class DirectorHookBase(Hook):
    """
    director hook base class.

    all packages that need to be hooked in directors business, must implement
    this class and register an instance of it in director hooks.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a director is going to be deleted.

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

        director_services.delete(id)
