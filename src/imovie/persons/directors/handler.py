# -*- coding: utf-8 -*-
"""
directors handler module.
"""

import imovie.persons.directors.services as director_services

from imovie.persons.decorators import person_handler
from imovie.persons.enumerations import PersonTypeEnum
from imovie.persons.handler import AbstractPersonHandler


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
