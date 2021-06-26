# -*- coding: utf-8 -*-
"""
persons images services module.
"""

from pyrin.application.services import get_component

from charma.persons.images import PersonsImagesPackage


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

    :rtype: bool
    """

    return get_component(PersonsImagesPackage.COMPONENT_NAME).exists(name)


def delete(id):
    """
    deletes the photo of given person.

    :param uuid.UUID id: person id.

    :raises PersonDoesNotExistError: person does not exist error.
    """

    return get_component(PersonsImagesPackage.COMPONENT_NAME).delete(id)
