# -*- coding: utf-8 -*-
"""
persons images hooks module.
"""

import charma.persons.images.services as person_image_services

from charma.persons.decorators import person_hook
from charma.persons.hooks import PersonHookBase


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

        person_image_services.delete(id)
