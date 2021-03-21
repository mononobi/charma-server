# -*- coding: utf-8 -*-
"""
genres services module.
"""

from pyrin.application.services import get_component

from imovie.genres import GenresPackage


def get(id):
    """
    gets genre with given id.

    it raises an error if genre does not exist.

    :param uuid.UUID id: genre id.

    :raises GenreDoesNotExistError: genre does not exist error.

    :rtype: GenreEntity
    """

    return get_component(GenresPackage.COMPONENT_NAME).get(id)


def create(name, **options):
    """
    creates a new genre.

    :param str name: genre name.

    :raises ValidationError: validation error.

    :returns: created genre id.
    :rtype: uuid.UUID
    """

    return get_component(GenresPackage.COMPONENT_NAME).create(name, **options)


def find(**filters):
    """
    finds genres with given filters.

    :keyword str name: genre name.
    :keyword bool is_main: is main genre.

    :raises ValidationError: validation error.

    :rtype: list[GenreEntity]
    """

    return get_component(GenresPackage.COMPONENT_NAME).find(**filters)


def exists(name):
    """
    gets a value indicating that a genre with given name exists.

    :param str name: genre name.

    :rtype: bool
    """

    return get_component(GenresPackage.COMPONENT_NAME).exists(name)


def get_all():
    """
    gets all genres.

    :rtype: list[GenreEntity]
    """

    return get_component(GenresPackage.COMPONENT_NAME).get_all()


def delete(id):
    """
    deletes a genre with given id.

    :param uuid.UUID id: genre id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(GenresPackage.COMPONENT_NAME).delete(id)


def get_by_name(name):
    """
    gets a genre by name.

    it returns None if genre does not exist.

    :param str name: genre name.

    :rtype: GenreEntity
    """

    return get_component(GenresPackage.COMPONENT_NAME).get_by_name(name)
