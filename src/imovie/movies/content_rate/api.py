# -*- coding: utf-8 -*-
"""
movies content rate api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.content_rate.services as content_rate_services


@api('/movies/content-rates/<uuid:id>', authenticated=False)
def get(id, **options):
    """
    gets content rate with given id.

    it raises an error if content rate does not exist.

    :param uuid.UUID id: content rate id.

    :raises ContentRateDoesNotExistError: content rate does not exist error.

    :rtype: ContentRateEntity
    """

    return content_rate_services.get(id)


@api('/movies/content-rates', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, **options):
    """
    creates a new content rate.

    :param str name: content rate name.

    :raises ValidationError: validation error.

    :returns: created content rate id.
    :rtype: uuid.UUID
    """

    return content_rate_services.create(name, **options)


@api('/movies/content-rates', authenticated=False)
def find(**filters):
    """
    finds content rates with given filters.

    :keyword str name: content rate name.

    :raises ValidationError: validation error.

    :rtype: list[ContentRateEntity]
    """

    return content_rate_services.find(**filters)


@api('/movies/content-rates/all', authenticated=False)
def get_all(**options):
    """
    gets all content rates.

    :rtype: list[ContentRateEntity]
    """

    return content_rate_services.get_all()


@api('/movies/content-rates/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a content rate with given id.

    :param uuid.UUID id: content rate id.

    :returns: count of deleted items.
    :rtype: int
    """

    return content_rate_services.delete(id)
