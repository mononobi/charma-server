# -*- coding: utf-8 -*-
"""
persons api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.persons.services as persons_services


@api('/persons/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets person with given id.

    it raises an error if person does not exist.

    :param uuid.UUID id: person id.

    :raises PersonDoesNotExistError: person does not exist error.

    :rtype: PersonEntity
    """

    return persons_services.get(id)


@api('/persons', methods=HTTPMethodEnum.POST, authenticated=False)
def create(fullname, **options):
    """
    creates a new person.

    :param str fullname: fullname.

    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.

    :keyword str | list[str] type: person type to be used.
                                   defaults to None if not provided.

    :raises ValidationError: validation error.

    :returns: created person id.
    :rtype: uuid.UUID
    """

    return persons_services.create(fullname, **options)


@api('/persons/<uuid:id>', methods=HTTPMethodEnum.PATCH, authenticated=False)
def update(id, **options):
    """
    updates a person with given id.

    :param uuid.UUID id: person id.

    :keyword str fullname: fullname.
    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.

    :keyword str | list[str] type: person type to be used.
                                   defaults to None if not provided.

    :raises ValidationError: validation error.
    :raises PersonDoesNotExistError: person does not exist error.
    """

    return persons_services.update(id, **options)


@api('/persons', authenticated=False, paged=True, indexed=True)
def find(**filters):
    """
    finds persons with given filters.

    :keyword str fullname: fullname.
    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.
    :keyword datetime from_created_on: from created on.
    :keyword datetime to_created_on: to created on.

    :keyword bool consider_begin_of_day: specifies that consider begin
                                         of day for lower datetime.
                                         defaults to True if not provided.

    :keyword bool consider_end_of_day: specifies that consider end
                                       of day for upper datetime.
                                       defaults to True if not provided.

    :rtype: list[PersonEntity]
    """

    return persons_services.find(**filters)


@api('/persons/all', authenticated=False, paged=True, indexed=True)
def get_all(**options):
    """
    gets all persons.

    :rtype: list[PersonEntity]
    """

    return persons_services.get_all()


@api('/persons/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a person with given id.

    :param uuid.UUID id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return persons_services.delete(id)


@api('/persons/exists', methods=HTTPMethodEnum.GET, authenticated=False)
def exists(**options):
    """
    gets a value indicating that a person exists.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: bool
    """

    return persons_services.exists(**options)


@api('/persons/try', methods=HTTPMethodEnum.GET, authenticated=False)
def try_get(**options):
    """
    gets a person with given imdb page link or fullname.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.
    it returns None if person not found.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: PersonEntity
    """

    return persons_services.try_get(**options)
