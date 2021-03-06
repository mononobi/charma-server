# -*- coding: utf-8 -*-
"""
directors services module.
"""

from pyrin.application.services import get_component

from imovie.persons.directors import DirectorsPackage


def get(id):
    """
    gets director with given id.

    it raises an error if director does not exist.

    :param uuid.UUID id: person id.

    :raises DirectorDoesNotExistError: director does not exist error.

    :rtype: PersonEntity
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).get(id)


def create(id, **options):
    """
    creates a new director.

    :param uuid.UUID id: person id.
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).create(id, **options)


def delete(id):
    """
    deletes a director with given id.

    :param uuid.UUID id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).delete(id)


def find(**filters):
    """
    finds directors with given filters.

    :keyword str fullname: fullname.
    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.
    :keyword datetime from_created_on: from created on.
    :keyword datetime to_created_on: to created on.

    :keyword bool consider_begin_of_day: specifies that consider begin
                                         of day for lower datetime.
                                         defaults to False if not provided.

    :keyword bool consider_end_of_day: specifies that consider end
                                       of day for upper datetime.
                                       defaults to False if not provided.

    :rtype: list[PersonEntity]
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).find(**filters)


def exists(**options):
    """
    gets a value indicating that a director exists.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: bool
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).exists(**options)


def get_all():
    """
    gets all directors.

    :rtype: list[PersonEntity]
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).get_all()


def try_get(**options):
    """
    gets a director with given imdb page link or fullname.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.
    it returns None if director not found.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: PersonEntity
    """

    return get_component(DirectorsPackage.COMPONENT_NAME).try_get(**options)
