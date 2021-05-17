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
