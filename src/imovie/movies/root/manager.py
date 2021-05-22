# -*- coding: utf-8 -*-
"""
movies root manager module.
"""

import os

import pyrin.validator.services as validator_services
import pyrin.utils.environment as env_utils
import pyrin.utils.path as path_utils

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.movies.root.models import MovieRootPathEntity
from imovie.movies.root import MovieRootPackage
from imovie.movies.root.exceptions import MovieRootPathAlreadyExistedError, \
    OSTypeIsUnknownError


class MovieRootManager(Manager):
    """
    movie root manager class.
    """

    package_class = MovieRootPackage

    def _exists(self, path, operating_system, **options):
        """
        gets a value indicating that given path for provided os is already existed.

        :param str path: root path.
        :param int operating_system: operating system of given path.
        :enum operating_system:
            LINUX = 0
            WINDOWS = 1
            MAC = 2
            JAVA = 3

        :rtype: bool
        """

        store = get_current_store()
        return store.query(MovieRootPathEntity.id)\
            .filter(MovieRootPathEntity.os == operating_system,
                    MovieRootPathEntity.path.ilike(path))\
            .existed()

    def create(self, path, **options):
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

        operating_system = self.get_current_os()
        options.update(path=path, os=operating_system)
        validator_services.validate_dict(MovieRootPathEntity, options)
        path_utils.assert_is_directory(path)
        if self._exists(path, operating_system) is True:
            raise MovieRootPathAlreadyExistedError(_('Movie root path [{root}] is '
                                                     'already existed.'.format(root=path)))

        entity = MovieRootPathEntity(**options)
        entity.save()
        return entity.id

    def delete(self, id, **options):
        """
        deletes a movie root path.

        it returns the count of deleted items.

        :param uuid.UUID id: root path id to be deleted.

        :rtype: int
        """

        validator_services.validate_field(MovieRootPathEntity, 'id', id)
        store = get_current_store()
        return store.query(MovieRootPathEntity)\
            .filter(MovieRootPathEntity.id == id).delete()

    def get_all(self, **options):
        """
        gets all root paths for current os.

        :rtype: list[MovieRootPathEntity]
        """

        operating_system = self.get_current_os()
        store = get_current_store()
        return store.query(MovieRootPathEntity).filter(
            MovieRootPathEntity.os == operating_system).all()

    def get_current_os(self, **options):
        """
        gets current os from `OSEnum` values.

        it raises an error if os type could not be determined.

        :raises OSTypeIsUnknownError: os type is unknown error.

        :rtype: int
        """

        if env_utils.is_linux():
            return MovieRootPathEntity.OSEnum.LINUX

        if env_utils.is_windows():
            return MovieRootPathEntity.OSEnum.WINDOWS

        if env_utils.is_mac():
            return MovieRootPathEntity.OSEnum.MAC

        if env_utils.is_java():
            return MovieRootPathEntity.OSEnum.JAVA

        raise OSTypeIsUnknownError(_('Operating system is unknown.'))

    def get_full_path(self, directory, **options):
        """
        gets the full path for given movie directory name.

        it returns a list of paths if any found.
        it may return None if nothing found.

        :param str directory: movie directory name.

        :rtype: list[str]
        """

        results = []
        roots = self.get_all(**options)
        for item in roots:
            full_path = os.path.join(item.path, directory)
            if os.path.exists(full_path):
                results.append(full_path)

        if len(results) > 0:
            return results

        return None
