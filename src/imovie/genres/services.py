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

    :param int id: genre id.

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
    :rtype: int
    """

    return get_component(GenresPackage.COMPONENT_NAME).create(name, **options)


def find(**filters):
    """
    finds genres with given filters.

    :keyword str name: genre name.
    :keyword bool is_main: is main genre.

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
