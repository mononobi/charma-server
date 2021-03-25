# -*- coding: utf-8 -*-
"""
movies collector manager module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services
import pyrin.configuration.services as config_services
import pyrin.utils.path as pyrin_path_utils

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

import imovie.media_info.services as media_info_services
import imovie.movies.services as movie_services
import imovie.utils.path as path_utils

from imovie.movies.models import MovieEntity
from imovie.movies.collector import MoviesCollectorPackage
from imovie.movies.collector.enumerations import MovieNormalizerEnum
from imovie.movies.collector.exceptions import DirectoryIsIgnoredError, \
    MovieIsAlreadyCollectedError


class MoviesCollectorManager(Manager):
    """
    movies collector manager class.
    """

    package_class = MoviesCollectorPackage

    # the minimum quality of movie to be considered in the relevant category.
    MIN_QUALITY = 0.65
    VCD_THRESHOLD = int(352 * 240 * MIN_QUALITY)
    DVD_THRESHOLD = int(720 * 480 * MIN_QUALITY)
    HD_THRESHOLD = int(1280 * 720 * MIN_QUALITY)
    FHD_THRESHOLD = int(1920 * 1080 * MIN_QUALITY)
    QHD_THRESHOLD = int(2560 * 1440 * MIN_QUALITY)
    UHD_THRESHOLD = int(3840 * 2160 * MIN_QUALITY)

    def __init__(self):
        """
        initializes an instance of MoviesCollectorManager.
        """

        super().__init__()

        self._video_extensions = self._get_video_extensions()
        self._ignored_chars = self._get_ignored_chars()
        self._remove_chars = self._get_remove_chars()

    def _get_video_extensions(self):
        """
        gets all valid video extensions from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('media.info', 'general', 'video_extensions')
        result = [item.lower() for item in result]
        return tuple(set(result))

    def _get_ignored_chars(self):
        """
        gets all ignored chars from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('media.info', 'general', 'video_extensions')
        return tuple(set(result))

    def _get_remove_chars(self):
        """
        gets all remove chars from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('media.info', 'general', 'remove_chars')
        result = [item.lower() for item in result]
        return tuple(set(result))

    def _should_be_ignored(self, directory):
        """
        gets a value indicating that a movie with given directory name must be ignored.

        :param str directory: directory name.

        :rtype: bool
        """

        return directory.startswith(self._ignored_chars)

    def _normalize_name(self, name, **options):
        """
        normalizes given movie name.

        :param str name: movie name.

        :rtype: str
        """

        name = name.strip()
        name = normalizer_services.normalize(name,
                                             MovieNormalizerEnum.MOVIE_NAME_METADATA,
                                             NormalizerEnum.DUPLICATE_SPACE,
                                             filters=self._remove_chars)
        name = name.strip('-')
        name = name.strip()
        return name

    def collect(self, directory, **options):
        """
        collects the movie from given directory into database.

        :param str directory: directory path of movie.

        :keyword bool force: specifies that movie must be forcefully collected
                             even if size or runtime conditions are not met.
                             defaults to False if not provided.

        :raises InvalidPathError: invalid path error.
        :raises PathIsNotAbsoluteError: path is not absolute error.
        :raises PathNotExistedError: path not existed error.
        :raises IsNotDirectoryError: is not directory error.
        :raises DirectoryIsIgnoredError: directory is ignored error.
        :raises MovieIsAlreadyCollectedError: movie is already collected error.
        """

        pyrin_path_utils.assert_is_directory(directory)
        force = options.get('force', False)
        fullname = path_utils.get_last_directory(directory)
        if force is not True and self._should_be_ignored(fullname) is True:
            raise DirectoryIsIgnoredError(_('Directory [{directory}] is ignored.')
                                          .format(directory=fullname))

        if movie_services.exists_by_directory(fullname) is True:
            raise MovieIsAlreadyCollectedError(_('Movie [{movie}] is already collected.')
                                               .format(movie=fullname))

    def get_quality(self, width, height, **options):
        """
        gets the video quality based on given resolution.

        :param int width: width.
        :param int height: height.

        :returns: video quality.
        :enum video quality:
            UNKNOWN = 0
            VCD = 1
            DVD = 2
            HD = 3
            FHD = 4
            QHD = 5
            UHD = 6

        :rtype: int
        """

        if width in (None, 0) or height in (None, 0):
            return MovieEntity.ResolutionEnum.UNKNOWN

        quality = width * height
        if quality >= self.UHD_THRESHOLD:
            return MovieEntity.ResolutionEnum.UHD

        if quality >= self.QHD_THRESHOLD:
            return MovieEntity.ResolutionEnum.QHD

        if quality >= self.FHD_THRESHOLD:
            return MovieEntity.ResolutionEnum.FHD

        if quality >= self.HD_THRESHOLD:
            return MovieEntity.ResolutionEnum.HD

        if quality >= self.DVD_THRESHOLD:
            return MovieEntity.ResolutionEnum.DVD

        if quality >= self.VCD_THRESHOLD:
            return MovieEntity.ResolutionEnum.VCD

        return MovieEntity.ResolutionEnum.UNKNOWN
