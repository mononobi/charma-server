# -*- coding: utf-8 -*-
"""
movies images services module.
"""

from pyrin.application.services import get_component

from imovie.movies.images import MoviesImagesPackage


def get_root_directory():
    """
    gets the root directory for images.

    :rtype: str
    """

    return get_component(MoviesImagesPackage.COMPONENT_NAME).get_root_directory()


def get_full_path(name):
    """
    gets the full path of image with given name.

    :param str name: image name.

    :rtype: str
    """

    return get_component(MoviesImagesPackage.COMPONENT_NAME).get_full_path(name)


def exists(name):
    """
    gets a value indicating that an image with given name exists.

    :param str name: image name.

    :rtype: bool
    """

    return get_component(MoviesImagesPackage.COMPONENT_NAME).exists(name)


def delete(id):
    """
    deletes the poster image of given movie.

    :param uuid.UUID id: movie id.

    :raises MovieDoesNotExistError: movie does not exist error.
    """

    return get_component(MoviesImagesPackage.COMPONENT_NAME).delete(id)
