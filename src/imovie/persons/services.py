# -*- coding: utf-8 -*-
"""
persons services module.
"""

from pyrin.application.services import get_component

from imovie.persons import PersonsPackage


def get_fullname(first_name, last_name):
    """
    gets full name from given inputs.

    :param str first_name: first name.
    :param str last_name: last name.

    :rtype: str
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get_fullname(first_name, last_name)


def get(id):
    """
    gets person with given id.

    it raises an error if person does not exist.

    :param int id: person id.

    :raises PersonDoesNotExistError: person does not exist error.

    :rtype: PersonEntity
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get(id)


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

    return get_component(PersonsPackage.COMPONENT_NAME).create(first_name, **options)


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

    return get_component(PersonsPackage.COMPONENT_NAME).find(**filters)


def exists(first_name, last_name):
    """
    gets a value indicating that a person with given first and last name exists.

    :param str first_name: first name.
    :param str last_name: last name

    :rtype: bool
    """

    return get_component(PersonsPackage.COMPONENT_NAME).exists(first_name, last_name)


def get_all():
    """
    gets all persons.

    :rtype: list[PersonEntity]
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get_all()


def delete(id):
    """
    deletes a person with given id.

    :param int id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(PersonsPackage.COMPONENT_NAME).delete(id)


def get_by_name(first_name, last_name):
    """
    gets a person by its first and last name.

    it returns None if person does not exist.

    :param str first_name: first name.
    :param str last_name: last name

    :rtype: PersonEntity
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get_by_name(first_name, last_name)
