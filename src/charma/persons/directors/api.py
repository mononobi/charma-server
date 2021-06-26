# -*- coding: utf-8 -*-
"""
directors api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.persons.directors.services as director_services


@api('/directors/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets director with given id.

    it raises an error if director does not exist.

    :param uuid.UUID id: person id.

    :raises DirectorDoesNotExistError: director does not exist error.

    :rtype: PersonEntity
    """

    return director_services.get(id)


@api('/directors', methods=HTTPMethodEnum.POST, authenticated=False)
def create(id, **options):
    """
    creates a new director.

    :param uuid.UUID id: person id.
    """

    return director_services.create(id, **options)


@api('/directors/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a director with given id.

    :param uuid.UUID id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return director_services.delete(id)


@api('/directors', authenticated=False, paged=True, indexed=True)
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

    return director_services.find(**filters)


@api('/directors/all', authenticated=False, paged=True, indexed=True)
def get_all(**options):
    """
    gets all directors.

    :rtype: list[PersonEntity]
    """

    return director_services.get_all()
