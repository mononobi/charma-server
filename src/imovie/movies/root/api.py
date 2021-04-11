# -*- coding: utf-8 -*-
"""
movies root api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.root.services as movie_root_services


@api('/movies/roots', methods=HTTPMethodEnum.POST, authenticated=False)
def create(path, **options):
    """
    creates a movie root path.

    :param str path: root path.

    :raises MovieRootPathAlreadyExistedError: movie root path already existed error.

    :rtype: uuid.UUID
    """

    return movie_root_services.create(path, **options)


@api('/movies/roots/<uuid:id>', methods=HTTPMethodEnum.DELETE, authenticated=False)
def delete(id, **options):
    """
    deletes a movie root path.

    it returns the count of deleted items.

    :param uuid.UUID id: root path id to be deleted.

    :rtype: int
    """

    return movie_root_services.delete(id, **options)


@api('/movies/roots', authenticated=False)
def get_all(**options):
    """
    gets all root paths for current os.

    :rtype: list[MovieRootPathEntity]
    """

    return movie_root_services.get_all(**options)
