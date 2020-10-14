# -*- coding: utf-8 -*-
"""
genres api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.genres.services as genres_services


@api('/genres/<int:id>', authenticated=False)
def get(id, **options):
    """
    gets genre with given id.

    it raises an error if genre does not exist.

    :param int id: genre id.

    :raises GenreDoesNotExistError: genre does not exist error.

    :rtype: dict(int id,
                 str name,
                 bool is_main)
    """

    return genres_services.get(id)


@api('/genres', methods=HTTPMethodEnum.POST, authenticated=False)
def create(name, **options):
    """
    creates a new genre.

    :param str name: genre name.

    :raises ValidationError: validation error.

    :returns: created genre id.
    :rtype: int
    """

    return genres_services.create(name, **options)


@api('/genres', authenticated=False)
def find(**filters):
    """
    finds genres with given filters.

    :keyword str name: genre name.
    :keyword bool is_main: is main genre.

    :returns: list[dict(int id,
                        str name,
                        bool is_main)]
    :rtype: list[dict]
    """

    return genres_services.find(**filters)


@api('/genres/all', authenticated=False)
def get_all(**options):
    """
    gets all genres.

    :returns: list[dict(int id,
                        str name,
                        bool is_main)]
    :rtype: list[dict]
    """

    return genres_services.get_all()
