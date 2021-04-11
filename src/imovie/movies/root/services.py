# -*- coding: utf-8 -*-
"""
movies root services module.
"""

from pyrin.application.services import get_component

from imovie.movies.root import MovieRootPackage


def create(path, **options):
    """
    creates a movie root path.

    :param str path: root path.

    :raises MovieRootPathAlreadyExistedError: movie root path already existed error.

    :rtype: uuid.UUID
    """

    return get_component(MovieRootPackage.COMPONENT_NAME).create(path, **options)


def delete(id, **options):
    """
    deletes a movie root path.

    it returns the count of deleted items.

    :param uuid.UUID id: root path id to be deleted.

    :rtype: int
    """

    return get_component(MovieRootPackage.COMPONENT_NAME).delete(id, **options)


def get_all(**options):
    """
    gets all root paths for current os.

    :rtype: list[MovieRootPathEntity]
    """

    return get_component(MovieRootPackage.COMPONENT_NAME).get_all(**options)


def get_current_os(**options):
    """
    gets current os from `OSEnum` values.

    it raises an error if os type could not be determined.

    :raises OSTypeIsUnknownError: os type is unknown error.

    :rtype: int
    """

    return get_component(MovieRootPackage.COMPONENT_NAME).get_current_os(**options)
