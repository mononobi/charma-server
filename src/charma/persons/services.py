# -*- coding: utf-8 -*-
"""
persons services module.
"""

from pyrin.application.services import get_component

from charma.persons import PersonsPackage


def register_handler(instance, **options):
    """
    registers a person handler.

    :param AbstractPersonHandler instance: handler instance.

    :raises InvalidPersonHandlerTypeError: invalid person handler type error.
    :raises PersonHandlerNameRequiredError: person handler name required error.
    :raises DuplicatedPersonHandlerError: duplicated person handler error.
    """

    return get_component(PersonsPackage.COMPONENT_NAME).register_handler(instance, **options)


def register_hook(instance):
    """
    registers the given instance into person hooks.

    :param PersonHookBase instance: person hook instance to be registered.

    :raises InvalidPersonHookTypeError: invalid person hook type error.
    """

    return get_component(PersonsPackage.COMPONENT_NAME).register_hook(instance)


def get(id):
    """
    gets person with given id.

    it raises an error if person does not exist.

    :param uuid.UUID id: person id.

    :raises PersonDoesNotExistError: person does not exist error.

    :rtype: PersonEntity
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get(id)


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

    return get_component(PersonsPackage.COMPONENT_NAME).create(fullname, **options)


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

    return get_component(PersonsPackage.COMPONENT_NAME).update(id, **options)


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
                                         defaults to False if not provided.

    :keyword bool consider_end_of_day: specifies that consider end
                                       of day for upper datetime.
                                       defaults to False if not provided.

    :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                    to be used in select list.
                                                    if not provided, `PersonEntity`
                                                    will be used.

    :keyword list[str] | str order_by: order by columns.

    :rtype: list[PersonEntity]
    """

    return get_component(PersonsPackage.COMPONENT_NAME).find(**filters)


def exists(**options):
    """
    gets a value indicating that a person exists.

    it searches using given imdb page link but if it
    fails, it searches with given name if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str fullname: fullname.

    :rtype: bool
    """

    return get_component(PersonsPackage.COMPONENT_NAME).exists(**options)


def get_all(**options):
    """
    gets all persons.

    :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                    to be used in select list.
                                                    if not provided, `PersonEntity`
                                                    will be used.

    :keyword list[str] | str order_by: order by columns.

    :rtype: list[PersonEntity]
    """

    return get_component(PersonsPackage.COMPONENT_NAME).get_all(**options)


def delete(id):
    """
    deletes a person with given id.

    :param uuid.UUID id: person id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(PersonsPackage.COMPONENT_NAME).delete(id)


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

    return get_component(PersonsPackage.COMPONENT_NAME).try_get(**options)
