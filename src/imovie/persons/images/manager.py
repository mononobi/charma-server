# -*- coding: utf-8 -*-
"""
persons images manager module.
"""

import pyrin.configuration.services as config_services

from imovie.images.manager import ImagesManager
from imovie.persons.images import PersonsImagesPackage


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
