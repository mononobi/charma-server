# -*- coding: utf-8 -*-
"""
movies collector manager module.
"""

import os
import re

import pyrin.utils.path as path_utils
import pyrin.utils.slug as slug_utils
import pyrin.utils.regex as regex_utils
import pyrin.logging.services as logging_services
import pyrin.configuration.services as config_services
import pyrin.globalization.datetime.services as datetime_services
import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

import imovie.media_info.services as media_info_services
import imovie.movies.services as movie_services

from imovie.movies.models import MovieEntity
from imovie.movies.collector import MoviesCollectorPackage
from imovie.movies.collector.enumerations import MovieNormalizerEnum
from imovie.movies.collector.exceptions import DirectoryIsIgnoredError, \
    MovieIsAlreadyCollectedError, DirectoryIsEmptyError, InvalidMovieTitleError


class MoviesCollectorManager(Manager):
    """
    movies collector manager class.
    """

    LOGGER = logging_services.get_logger('movie.collector')
    package_class = MoviesCollectorPackage

    # the minimum quality for movie to be considered in the relevant category.
    MIN_QUALITY = 0.65
    VCD_THRESHOLD = int(352 * 240 * MIN_QUALITY)
    DVD_THRESHOLD = int(720 * 480 * MIN_QUALITY)
    HD_THRESHOLD = int(1280 * 720 * MIN_QUALITY)
    FHD_THRESHOLD = int(1920 * 1080 * MIN_QUALITY)
    QHD_THRESHOLD = int(2560 * 1440 * MIN_QUALITY)
    UHD_THRESHOLD = int(3840 * 2160 * MIN_QUALITY)

    # a regex to match year in movie folder name.
    # it matches all years from 1900 to 2999.
    YEAR_REGEX = re.compile('(19[0-9]{2})|(2[0-9]{3})', flags=re.IGNORECASE)

    # this slug will be appended to folder name on preparing individual files
    # if a folder with the same name exists and will be removed at the end.
    TEMP_SLUG = 'beginslug{digits}endslug'

    # this slug will be appended to folder name when a movie with the
    # same directory name is already existed.
    SEQUENCE_SLUG = ' -D{digits}'

    def __init__(self):
        """
        initializes an instance of MoviesCollectorManager.
        """

        super().__init__()

        self._video_extensions = self._get_video_extensions()
        self._ignored_chars = self._get_ignored_chars()
        self._remove_chars = self._get_remove_chars()
        self._min_size = config_services.get('movies', 'collector', 'min_size')
        self._min_runtime = config_services.get('movies', 'collector', 'min_runtime')

    def _get_video_extensions(self):
        """
        gets all valid video extensions from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('movies', 'collector', 'video_extensions')
        result = [item.lower() for item in result]
        return tuple(set(result))

    def _get_ignored_chars(self):
        """
        gets all ignored chars from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('movies', 'collector', 'ignored_chars')
        return tuple(set(result))

    def _get_remove_chars(self):
        """
        gets all remove chars from config store.

        :rtype: tuple[str]
        """

        result = config_services.get('movies', 'collector', 'remove_chars')
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

        :keyword bool remove_sequence: specifies that sequence slug must be removed
                                       from name. defaults to True if not provided.

        :rtype: str
        """

        remove_sequence = options.get('remove_sequence', True)
        normalizers = [MovieNormalizerEnum.MOVIE_NAME_METADATA,
                       NormalizerEnum.DUPLICATE_SPACE,
                       NormalizerEnum.TITLE_CASE,
                       MovieNormalizerEnum.MOVIE_COUNTING_LETTER]

        if remove_sequence is not False:
            normalizers.insert(0, MovieNormalizerEnum.MOVIE_SEQUENCE_SLUG)

        name = name.strip()
        name = normalizer_services.normalize(name, *normalizers,
                                             filters=self._remove_chars)
        name = name.strip('-')
        name = name.strip()
        return name

    def _get_temp_slug(self):
        """
        gets a new temp slug.

        :rtype: str
        """

        digits = slug_utils.get_digit_slug(4)
        return self.TEMP_SLUG.format(digits=digits)

    def _get_sequence_slug(self):
        """
        gets a sequence slug to be used if a movie with the same folder is already existed.

        :rtype: str
        """

        digits = slug_utils.get_digit_slug(2)
        return self.SEQUENCE_SLUG.format(digits=digits)

    def _extract_year(self, name, **options):
        """
        extracts year from given movie name.

        it returns a tuple of two items. first item is the year and the
        second is the movie name without year.
        year may be None if it could not be extracted from movie name.

        :param str name: movie name.

        :returns: tuple[int year, str name]
        :rtype: tuple[int, str]
        """

        matches = regex_utils.matches(self.YEAR_REGEX, name)
        if len(matches) <= 0:
            return None, name

        # we consider the last found year as production year
        # because the movie may have a year in its name too.
        year = int(matches[-1])
        if year > datetime_services.current_year() + 1:
            return None, name

        index = name.rfind(str(year))
        new_name = name[0:index]
        new_name = new_name.strip()

        # if the found year is at the beginning, it will be
        # considered as movie name not production year.
        if index == 0 or len(new_name) <= 0:
            return None, name

        return year, new_name

    def _prepare_individual_files(self, root, **options):
        """
        prepares individual movie files in given path for collecting.

        :param str root: root directory.
        """

        files = path_utils.get_files(root, *self._video_extensions)
        for item in files:
            parent, name = path_utils.split_name(item)
            folder_name = path_utils.get_file_name(name, include_extension=False)
            folder = os.path.join(parent, folder_name)
            folder = self._get_unique_directory_name(folder, self._get_temp_slug)
            path_utils.create_directory(folder)
            target = os.path.join(folder, name)
            path_utils.move(item, target)

    def _get_unique_directory_name(self, directory, slug_generator, **options):
        """
        gets a unique directory name with given path.

        if the same directory is already existed, it uses the slug generator
        to produce a slug and append it to the original requested name.

        :param str directory: the full directory path to be created.
        :param function slug_generator: a callable to be used for slug generation.

        :keyword str old_directory: the original directory name that the movie is
                                    going to be collected from.
                                    it may be the same as `directory` or None.

        :rtype: str
        """

        old_directory = options.get('old_directory')
        if old_directory is None or not path_utils.is_same_path(directory, old_directory):
            last_slug = None
            old_name = directory
            while os.path.exists(directory) is True:
                if last_slug is not None:
                    directory = directory.rstrip(last_slug)

                last_slug = slug_generator()
                directory = directory + last_slug

            if last_slug is not None:
                self.LOGGER.info('Directory with name [{old_name}] is already existed. '
                                 'The new directory will be created with name [{new_name}].'
                                 .format(old_name=old_name, new_name=directory))
        return directory

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
        :raises InvalidMovieTitleError: invalid movie title error.
        :raises DirectoryIsEmptyError: directory is empty error.
        """

        path_utils.assert_is_directory(directory)
        force = options.get('force', False)
        parent_directory = path_utils.get_last_directory_name(directory)
        title = parent_directory
        if force is not True and self._should_be_ignored(title) is True:
            raise DirectoryIsIgnoredError(_('Directory [{directory}] is ignored.')
                                          .format(directory=directory))

        if movie_services.exists_by_directory(title) is True:
            raise MovieIsAlreadyCollectedError(_('Movie [{movie}] is already collected.')
                                               .format(movie=title))

        title = self._normalize_name(title)
        year, title = self._extract_year(title)

        # we have to re-normalize the name after extracting year from it.
        title = self._normalize_name(title, remove_sequence=False)

        if len(title) <= 0:
            raise InvalidMovieTitleError(_('Movie [{directory}] does not have a valid title.')
                                         .format(directory=directory))

        total_runtime = 0
        total_width = 0
        total_height = 0
        collected_count = 0
        movies = path_utils.get_files(directory, *self._video_extensions)
        for item in movies:
            result = media_info_services.get_info(item)
            size = path_utils.get_file_size(item)
            runtime = result.get('runtime')
            width = result.get('width')
            height = result.get('height')
            if force is not True and size < self._min_size and runtime < self._min_runtime:
                continue

            collected_count += 1
            total_runtime += runtime
            total_width += width
            total_height += height

        if collected_count <= 0:
            raise DirectoryIsEmptyError(_('Directory [{directory}] is empty.')
                                        .format(directory=directory))

        total_runtime = int(total_runtime / collected_count)
        total_width = int(total_width / collected_count)
        total_height = int(total_height / collected_count)
        quality = self.get_quality(total_width, total_height)
        fullname = movie_services.get_fullname(title, year, quality)
        root, name = path_utils.split_name(directory)
        new_path = os.path.join(root, fullname)
        new_path = self._get_unique_directory_name(new_path, self._get_sequence_slug,
                                                   old_directory=directory)
        fullname = path_utils.get_directory_name(new_path)
        new_path = path_utils.rename(directory, fullname)

        # we have to rename directory to its original name if movie creation failed.
        try:
            movie_services.create(title, fullname, production_year=year,
                                  runtime=total_runtime, resolution=quality)
        except Exception as error:
            path_utils.rename(new_path, parent_directory)
            raise error

    def collect_all(self, root, **options):
        """
        collects all movies in root directory.

        :param str root: root directory.

        :keyword bool include_individual_files: specifies that individual movie files in the
                                                root path that have no directory must also be
                                                collected as movies.
                                                defaults to True if not provided.

        :raises InvalidPathError: invalid path error.
        :raises PathIsNotAbsoluteError: path is not absolute error.
        :raises PathNotExistedError: path not existed error.
        :raises IsNotDirectoryError: is not directory error.
        """

        path_utils.assert_is_directory(root)
        include_individual_files = options.get('include_individual_files', True)
        if include_individual_files is not False:
            self._prepare_individual_files(root, **options)

        directories = path_utils.get_directories(root)
        collected = 0
        ignored = 0
        already_collected = 0
        empty = 0
        failed = 0
        for item in directories:
            try:
                self.collect(item)
                collected += 1

            except DirectoryIsIgnoredError as error:
                ignored += 1
                self.LOGGER.exception(str(error))

            except MovieIsAlreadyCollectedError as error:
                already_collected += 1
                self.LOGGER.exception(str(error))

            except DirectoryIsEmptyError as error:
                empty += 1
                self.LOGGER.exception(str(error))

            except Exception as error:
                failed += 1
                self.LOGGER.exception(str(error))

        return dict(total=collected + ignored + already_collected + empty + failed,
                    collected=collected,
                    ignored=ignored,
                    already_collected=already_collected,
                    empty=empty,
                    failed=failed)

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

        quality = int(width * height)
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
