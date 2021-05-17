# -*- coding: utf-8 -*-
"""
persons images services module.
"""

from pyrin.application.services import get_component

from imovie.persons.images import PersonsImagesPackage


def get_root_directory():
    """
    gets the root directory for images.

    :rtype: str
    """

    return get_component(PersonsImagesPackage.COMPONENT_NAME).get_root_directory()


def get_full_path(name):
    """
    gets the full path of image with given name.

    :param str name: image name.

    :rtype: str
    """

    return get_component(PersonsImagesPackage.COMPONENT_NAME).get_full_path(name)


def exists(name):
    """
    gets a value indicating that an image with given name exists.

    :param str name: image name.
    """

    return get_component(PersonsImagesPackage.COMPONENT_NAME).exists(name)
