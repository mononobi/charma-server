# -*- coding: utf-8 -*-
"""
movies collector services module.
"""

from pyrin.application.services import get_component

from imovie.movies.collector import MoviesCollectorPackage


def collect(directory, **options):
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

    return get_component(MoviesCollectorPackage.COMPONENT_NAME).collect(directory, **options)


def collect_all(root, **options):
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

    :returns: dict(int total: total processed movies count,
                   int collected: collected movies count,
                   int ignored: ignored folders count,
                   int already_existed: already existed movies count,
                   int empty: empty folders count,
                   int failed: failed movies count)
    :rtype: dict
    """

    return get_component(MoviesCollectorPackage.COMPONENT_NAME).collect_all(root, **options)


def get_quality(width, height, **options):
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

    return get_component(MoviesCollectorPackage.COMPONENT_NAME).get_quality(width, height,
                                                                            **options)
