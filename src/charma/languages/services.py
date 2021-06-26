# -*- coding: utf-8 -*-
"""
languages services module.
"""

from pyrin.application.services import get_component

from charma.languages import LanguagesPackage


def get(id):
    """
    gets language with given id.

    it raises an error if language does not exist.

    :param int id: language id.

    :raises LanguageDoesNotExistError: language does not exist error.

    :rtype: LanguageEntity
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).get(id)


def create(name, **options):
    """
    creates a new language.

    :param str name: language name.

    :raises ValidationError: validation error.

    :returns: created language id.
    :rtype: int
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).create(name, **options)


def find(**filters):
    """
    finds languages with given filters.

    :keyword str name: language name.

    :raises ValidationError: validation error.

    :rtype: list[LanguageEntity]
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).find(**filters)


def exists(name):
    """
    gets a value indicating that a language with given name exists.

    :param str name: language name.

    :rtype: bool
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).exists(name)


def get_all():
    """
    gets all languages.

    :rtype: list[LanguageEntity]
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).get_all()


def delete(id):
    """
    deletes a language with given id.

    :param int id: language id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).delete(id)


def get_by_name(name):
    """
    gets a language by name.

    it returns None if language does not exist.

    :param str name: language name.

    :rtype: LanguageEntity
    """

    return get_component(LanguagesPackage.COMPONENT_NAME).get_by_name(name)
