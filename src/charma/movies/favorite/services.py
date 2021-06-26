# -*- coding: utf-8 -*-
"""
movies favorite services module.
"""

from pyrin.application.services import get_component

from charma.movies.favorite import FavoriteMoviesPackage


def get(movie_id):
    """
    gets favorite movie with given id.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.

    :raises FavoriteMovieDoesNotExistError: favorite movie does not exist error.

    :rtype: FavoriteMovieEntity
    """

    return get_component(FavoriteMoviesPackage.COMPONENT_NAME).get(movie_id)


def create(movie_id, favorite_rate, **options):
    """
    creates a new favorite movie.

    :param uuid.UUID movie_id: movie id.
    :param int favorite_rate: favorite rate.

    :raises ValidationError: validation error.
    """

    return get_component(FavoriteMoviesPackage.COMPONENT_NAME).create(movie_id,
                                                                      favorite_rate,
                                                                      **options)


def update(movie_id, favorite_rate, **options):
    """
    updates a favorite movie.

    :param uuid.UUID movie_id: movie id.
    :param int favorite_rate: favorite rate.

    :raises ValidationError: validation error.
    """

    return get_component(FavoriteMoviesPackage.COMPONENT_NAME).update(movie_id,
                                                                      favorite_rate,
                                                                      **options)


def delete(movie_id, **options):
    """
    deletes a favorite movie.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(FavoriteMoviesPackage.COMPONENT_NAME).delete(movie_id, **options)
