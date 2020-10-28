# -*- coding: utf-8 -*-
"""
persons api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.persons.services as persons_services


@api('/persons/<int:id>', authenticated=False)
def get(id):
    """
    gets person with given id.

    it raises an error if person does not exist.

    :param int id: person id.

    :raises PersonDoesNotExistError: person does not exist error.

    :rtype: PersonEntity
    """

    return persons_services.get(id)


@api('/persons', methods=HTTPMethodEnum.POST, authenticated=False)
def create(first_name, **options):
    """
    creates a new person.

    :param str first_name: first name.

    :keyword str last_name: last name.
    :keyword str imdb_page: imdb page link.
    :keyword str photo_name: photo file name.

    :raises ValidationError: validation error.

    :returns: created person id.
    :rtype: int
    """

    return persons_services.create(first_name, **options)


@api('/persons', authenticated=False)
def find(**filters):
    """
    finds persons with given filters.

    :keyword str first_name: first name.
    :keyword str last_name: last name
    :keyword str imdb_page: imdb page link
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

    return persons_services.find(**filters)


@api('/persons/all', authenticated=False)
def get_all():
    """
    gets all persons.

    :rtype: list[PersonEntity]
    """

    return persons_services.get_all()


@api('/persons/<int:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id):
    """
    deletes a person with given id.

    :param int id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return persons_services.delete(id)
