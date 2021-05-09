# -*- coding: utf-8 -*-
"""
countries services module.
"""

from pyrin.application.services import get_component

from imovie.countries import CountriesPackage


def get(id):
    """
    gets country with given id.

    it raises an error if country does not exist.

    :param uuid.UUID id: country id.

    :raises CountryDoesNotExistError: country does not exist error.

    :rtype: CountryEntity
    """

    return get_component(CountriesPackage.COMPONENT_NAME).get(id)


def create(name, **options):
    """
    creates a new country.

    :param str name: country name.

    :raises ValidationError: validation error.

    :returns: created country id.
    :rtype: uuid.UUID
    """

    return get_component(CountriesPackage.COMPONENT_NAME).create(name, **options)


def find(**filters):
    """
    finds countries with given filters.

    :keyword str name: country name.

    :raises ValidationError: validation error.

    :rtype: list[CountryEntity]
    """

    return get_component(CountriesPackage.COMPONENT_NAME).find(**filters)


def exists(name):
    """
    gets a value indicating that a country with given name exists.

    :param str name: country name.

    :rtype: bool
    """

    return get_component(CountriesPackage.COMPONENT_NAME).exists(name)


def get_all():
    """
    gets all countries.

    :rtype: list[CountryEntity]
    """

    return get_component(CountriesPackage.COMPONENT_NAME).get_all()


def delete(id):
    """
    deletes a country with given id.

    :param uuid.UUID id: country id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(CountriesPackage.COMPONENT_NAME).delete(id)


def get_by_name(name):
    """
    gets a country by name.

    it returns None if country does not exist.

    :param str name: country name.

    :rtype: CountryEntity
    """

    return get_component(CountriesPackage.COMPONENT_NAME).get_by_name(name)
