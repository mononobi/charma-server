# -*- coding: utf-8 -*-
"""
movies images manager module.
"""

import pyrin.configuration.services as config_services

from imovie.images.manager import ImagesManager
from imovie.movies.images import MoviesImagesPackage


class MoviesImagesManager(ImagesManager):
    """
    movies images manager class.
    """

    package_class = MoviesImagesPackage

    def _get_root_directory(self):
        """
        gets the root directory for images.

        :rtype: str
        """

        return config_services.get('movies', 'images', 'root_directory')
