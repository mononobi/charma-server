# -*- coding: utf-8 -*-
"""
persons images manager module.
"""

import pyrin.configuration.services as config_services

import charma.persons.services as person_services

from charma.images.manager import ImagesManager
from charma.persons.images import PersonsImagesPackage


class PersonsImagesManager(ImagesManager):
    """
    persons images manager class.
    """

    package_class = PersonsImagesPackage

    def _get_root_directory(self):
        """
        gets the root directory for images.

        :rtype: str
        """

        return config_services.get('persons', 'images', 'root_directory')

    def delete(self, id):
        """
        deletes the photo of given person.

        :param uuid.UUID id: person id.

        :raises PersonDoesNotExistError: person does not exist error.
        """

        entity = person_services.get(id)
        if entity.photo_name is not None:
            self._delete(entity.photo_name)
