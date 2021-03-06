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


@api('/actors', authenticated=False, paged=True, indexed=True)
def find(**filters):
    """
    finds actors with given filters.

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

    return actors_services.find(**filters)


@api('/actors/all', authenticated=False, paged=True, indexed=True)
def get_all(**options):
    """
    gets all actors.

    :rtype: list[PersonEntity]
    """

    return actors_services.get_all()
