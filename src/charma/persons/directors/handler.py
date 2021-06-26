# -*- coding: utf-8 -*-
"""
directors handler module.
"""

import charma.persons.directors.services as director_services

from charma.persons.decorators import person_handler
from charma.persons.enumerations import PersonTypeEnum
from charma.persons.handler import AbstractPersonHandler


@person_handler()
class DirectorHandler(AbstractPersonHandler):
    """
    director handler class.
    """

    name = PersonTypeEnum.DIRECTOR

    def create(self, id, **options):
        """
        creates a director with given inputs.

        :param uuid.UUID id: person id.
        """

        director_services.create(id, **options)
