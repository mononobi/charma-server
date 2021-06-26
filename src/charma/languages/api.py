# -*- coding: utf-8 -*-
"""
languages api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.languages.services as language_services


@api('/languages/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets language with given id.

    it raises an error if language does not exist.

    :param int id: language id.

    :raises LanguageDoesNotExistError: language does not exist error.

    :rtype: LanguageEntity
    """

    return language_services.get(id)


@api('/languages', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, **options):
    """
    creates a new language.

    :param str name: language name.

    :raises ValidationError: validation error.

    :returns: created language id.
    :rtype: int
    """

    return language_services.create(name, **options)


@api('/languages', authenticated=False)
def find(**filters):
    """
    finds languages with given filters.

    :keyword str name: language name.

    :rtype: list[LanguageEntity]
    """

    return language_services.find(**filters)


@api('/languages/all', authenticated=False)
def get_all(**options):
    """
    gets all languages.

    :rtype: list[LanguageEntity]
    """

    return language_services.get_all()


@api('/languages/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a language with given id.

    :param int id: language id.

    :returns: count of deleted items.
    :rtype: int
    """

    return language_services.delete(id)
