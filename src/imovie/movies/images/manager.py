# -*- coding: utf-8 -*-
"""
movies images manager module.
"""

import pyrin.configuration.services as config_services

import imovie.movies.services as movie_services

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

    def delete(self, id):
        """
        deletes the poster image of given movie.

        :param uuid.UUID id: movie id.

        :raises MovieDoesNotExistError: movie does not exist error.
        """

        entity = movie_services.get(id)
        if entity.poster_name is not None:
            self._delete(entity.poster_name)
