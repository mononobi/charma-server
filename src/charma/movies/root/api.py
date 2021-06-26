# -*- coding: utf-8 -*-
"""
movies root api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.movies.root.services as movie_root_services


@api('/movies/roots', methods=HTTPMethodEnum.POST, authenticated=False)
def create(path, **options):
    """
    creates a movie root path.

    :param str path: root path.

    :raises InvalidPathError: invalid path error.
    :raises PathIsNotAbsoluteError: path is not absolute error.
    :raises PathNotExistedError: path not existed error.
    :raises IsNotDirectoryError: is not directory error.
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
