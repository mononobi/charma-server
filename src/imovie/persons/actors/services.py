# -*- coding: utf-8 -*-
"""
actors services module.
"""

from pyrin.application.services import get_component

from imovie.persons.actors import ActorsPackage


def get(id):
    """
    gets actor with given id.

    it raises an error if actor does not exist.

    :param int id: person id.

    :raises ActorDoesNotExistError: actor does not exist error.

    :rtype: PersonEntity
    """

    return get_component(ActorsPackage.COMPONENT_NAME).get(id)


def create(id, **options):
    """
    creates a new actor.

    :param int id: person id.
    """

    return get_component(ActorsPackage.COMPONENT_NAME).create(id, **options)


def delete(id):
    """
    deletes an actor with given id.

    :param int id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(ActorsPackage.COMPONENT_NAME).delete(id)


def find(**filters):
    """
    finds actors with given filters.

    :keyword str fullname: fullname.
    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.
    :keyword datetime from_add_date: from add date.
    :keyword datetime to_add_date: to add date.

    :keyword bool consider_begin_of_day: specifies that consider begin
                                         of day for lower datetime.
                                         defaults to True if not provided.

    :keyword bool consider_end_of_day: specifies that consider end
                                       of day for upper datetime.
                                       defaults to True if not provided.

    :rtype: list[PersonEntity]
    """

    return get_component(ActorsPackage.COMPONENT_NAME).find(**filters)


def exists(**options):
    """
    gets a value indicating that an actor exists.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: bool
    """

    return get_component(ActorsPackage.COMPONENT_NAME).exists(**options)


def get_all():
    """
    gets all actors.

    :rtype: list[PersonEntity]
    """

    return get_component(ActorsPackage.COMPONENT_NAME).get_all()


def try_get(**options):
    """
    gets an actor with given imdb page link or fullname.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.
    it returns None if actor not found.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: PersonEntity
    """

    return get_component(ActorsPackage.COMPONENT_NAME).try_get(**options)
