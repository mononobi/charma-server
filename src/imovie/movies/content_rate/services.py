# -*- coding: utf-8 -*-
"""
movies content rate services module.
"""

from pyrin.application.services import get_component

from imovie.movies.content_rate import ContentRatePackage


def get(id):
    """
    gets content rate with given id.

    it raises an error if content rate does not exist.

    :param uuid.UUID id: content rate id.

    :raises ContentRateDoesNotExistError: content rate does not exist error.

    :rtype: ContentRateEntity
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).get(id)


def create(name, **options):
    """
    creates a new content rate.

    :param str name: content rate name.

    :raises ValidationError: validation error.

    :returns: created content rate id.
    :rtype: uuid.UUID
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).create(name, **options)


def find(**filters):
    """
    finds content rates with given filters.

    :keyword str name: content rate name.

    :raises ValidationError: validation error.

    :rtype: list[ContentRateEntity]
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).find(**filters)


def exists(name):
    """
    gets a value indicating that a content rate with given name exists.

    :param str name: content rate name.

    :rtype: bool
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).exists(name)


def get_all():
    """
    gets all content rates.

    :rtype: list[ContentRateEntity]
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).get_all()


def delete(id):
    """
    deletes a content rate with given id.

    :param uuid.UUID id: content rate id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).delete(id)


def get_by_name(name):
    """
    gets a content rate by name.

    it returns None if content rate does not exist.

    :param str name: content rate name.

    :rtype: ContentRateEntity
    """

    return get_component(ContentRatePackage.COMPONENT_NAME).get_by_name(name)
