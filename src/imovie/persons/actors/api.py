# -*- coding: utf-8 -*-
"""
actors api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.persons.actors.services as actors_services


@api('/actors/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets actor with given id.

    it raises an error if actor does not exist.

    :param uuid.UUID id: person id.

    :raises ActorDoesNotExistError: actor does not exist error.

    :rtype: PersonEntity
    """

    return actors_services.get(id)


@api('/actors', methods=HTTPMethodEnum.POST, authenticated=False)
def create(id, **options):
    """
    creates a new actor.

    :param uuid.UUID id: person id.
    """

    return actors_services.create(id, **options)


@api('/actors/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes an actor with given id.

    :param uuid.UUID id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return actors_services.delete(id)


@api('/actors', authenticated=False)
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

    return actors_services.find(**filters)


@api('/actors/exists', methods=HTTPMethodEnum.GET, authenticated=False)
def exists(**options):
    """
    gets a value indicating that an actor exists.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: bool
    """

    return actors_services.exists(**options)


@api('/actors/all', authenticated=False)
def get_all(**options):
    """
    gets all actors.

    :rtype: list[PersonEntity]
    """

    return actors_services.get_all()


@api('/actors/try', methods=HTTPMethodEnum.GET, authenticated=False)
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

    return actors_services.try_get(**options)
