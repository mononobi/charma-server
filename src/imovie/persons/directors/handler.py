# -*- coding: utf-8 -*-
"""
directors handler module.
"""

import imovie.persons.directors.services as directors_services

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

        directors_services.create(id, **options)

    def delete(self, id, **options):
        """
        deletes the given director.

        :param uuid.UUID id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        directors_services.delete(id)
