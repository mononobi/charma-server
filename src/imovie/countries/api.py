# -*- coding: utf-8 -*-
"""
countries api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.countries.services as country_services


@api('/countries/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets country with given id.

    it raises an error if country does not exist.

    :param uuid.UUID id: country id.

    :raises CountryDoesNotExistError: country does not exist error.

    :rtype: CountryEntity
    """

    return country_services.get(id)


@api('/countries', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, **options):
    """
    creates a new country.

    :param str name: country name.

    :raises ValidationError: validation error.

    :returns: created country id.
    :rtype: uuid.UUID
    """

    return country_services.create(name, **options)


@api('/countries', authenticated=False)
def find(**filters):
    """
    finds countries with given filters.

    :keyword str name: country name.

    :raises ValidationError: validation error.

    :rtype: list[CountryEntity]
    """

    return country_services.find(**filters)


@api('/countries/all', authenticated=False)
def get_all(**options):
    """
    gets all countries.

    :rtype: list[CountryEntity]
    """

    return country_services.get_all()


@api('/countries/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a country with given id.

    :param uuid.UUID id: country id.

    :returns: count of deleted items.
    :rtype: int
    """

    return country_services.delete(id)
