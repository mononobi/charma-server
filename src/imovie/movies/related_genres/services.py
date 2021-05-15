# -*- coding: utf-8 -*-
"""
movies related genres services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_genres import RelatedGenresPackage


def get(movie_id, genre_id):
    """
    gets movie to genre with given ids.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID genre_id: genre id.

    :raises Movie2GenreDoesNotExistError: movie 2 genre does not exist error.

    :rtype: Movie2GenreEntity
    """

    return get_component(RelatedGenresPackage.COMPONENT_NAME).get(movie_id, genre_id)


def create(movie_id, genre_id, **options):
    """
    creates a new movie 2 genre record.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID genre_id: genre id.

    :keyword bool is_main: is main.

    :raises ValidationError: validation error.
    """

    return get_component(RelatedGenresPackage.COMPONENT_NAME).create(movie_id,
                                                                     genre_id, **options)


def delete(movie_id, genre_id, **options):
    """
    deletes a movie to genre record.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID genre_id: genre id.

    :rtype: int
    """

    return get_component(RelatedGenresPackage.COMPONENT_NAME).delete(movie_id,
                                                                     genre_id, **options)


def delete_by_movie(movie_id, **options):
    """
    deletes all movie to genre records of given movie id.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(RelatedGenresPackage.COMPONENT_NAME).delete_by_movie(movie_id,
                                                                              **options)


def exists(movie_id, **options):
    """
    gets a value indicating that given movie has any genres.

    :param uuid.UUID movie_id: movie id.

    :rtype: bool
    """

    return get_component(RelatedGenresPackage.COMPONENT_NAME).exists(movie_id, **options)
