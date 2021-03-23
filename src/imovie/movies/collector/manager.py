# -*- coding: utf-8 -*-
"""
movies collector manager module.
"""

import os

import pyrin.configuration.services as config_services

from pyrin.core.structs import Manager

import imovie.movies.services as movie_services
import imovie.utils.path as path_utils

from imovie.movies.collector import MoviesCollectorPackage
from imovie.movies.collector.enumerations import CollectResultEnum


class MoviesCollectorManager(Manager):
    """
    movies collector manager class.
    """

    package_class = MoviesCollectorPackage

    def __init__(self):
        """
        initializes an instance of MoviesCollectorManager.
        """

        super().__init__()

        self._ignored_chars = tuple(config_services.get('movies', 'collector', 'ignored_chars'))

    def _should_be_ignored(self, directory):
        """
        gets a value indicating that a movie with given directory name must be ignored.

        :param str directory: directory name.

        :rtype: bool
        """

        return directory.startswith(self._ignored_chars)

    def collect(self, directory, **options):
        """
        collects the movie from given directory into database.

        it may not collect anything on different conditions.
        it returns the collect result code.

        :param str directory: directory path of movie.

        :keyword bool force: specifies that movie must be forcefully collected
                             even if size or runtime conditions are not met.
                             defaults to False if not provided.

        :returns: collect result code from `CollectResultEnum`.

        :enum CollectResultEnum:
            UNKNOWN = 0
            EMPTY_FOLDER = 1
            ALREADY_EXISTED = 2
            IGNORED = 3
            COLLECTED = 4

        :rtype: int
        """

        if os.path.exists(directory) is False:
            raise

        if not os.path.isdir(directory):
            raise

        force = options.get('force', False)
        fullname = path_utils.get_last_directory(directory)
        if force is not True and self._should_be_ignored(fullname) is True:
            return CollectResultEnum.IGNORED

        if movie_services.exists_by_directory(directory) is True:
            return CollectResultEnum.ALREADY_EXISTED
