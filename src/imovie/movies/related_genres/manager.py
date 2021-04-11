# -*- coding: utf-8 -*-
"""
movies related genres manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from imovie.movies.models import Movie2GenreEntity
from imovie.movies.related_genres import RelatedGenresPackage
from imovie.movies.related_genres.exceptions import Movie2GenreDoesNotExistError


class RelatedGenresManager(Manager):
    """
    movies related genres manager class.
    """

    package_class = RelatedGenresPackage

    def _get(self, movie_id, genre_id):
        """
        gets movie to genre with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID genre_id: genre id.

        :rtype: Movie2GenreEntity
        """

        store = get_current_store()
        return store.query(Movie2GenreEntity).get((movie_id, genre_id))

    def get(self, movie_id, genre_id):
        """
        gets movie to genre with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID genre_id: genre id.

        :raises Movie2GenreDoesNotExistError: movie 2 genre does not exist error.

        :rtype: Movie2GenreEntity
        """

        entity = self._get(movie_id, genre_id)
        if entity is None:
            raise Movie2GenreDoesNotExistError(_('Movie to genre with movie id [{movie}] '
                                                 'and genre id [{genre}] does not exist.')
                                               .format(movie=movie_id, genre=genre_id))
        return entity

    def create(self, movie_id, genre_id, **options):
        """
        creates a new movie 2 genre record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID genre_id: genre id.

        :keyword bool is_main: is main.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, genre_id=genre_id, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(Movie2GenreEntity, options)
        entity = Movie2GenreEntity(**options)
        entity.save()

    def delete(self, movie_id, genre_id, **options):
        """
        deletes a movie to genre record.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID genre_id: genre id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2GenreEntity)\
            .filter(Movie2GenreEntity.movie_id == movie_id,
                    Movie2GenreEntity.genre_id == genre_id).delete()

    def delete_by_movie(self, movie_id, **options):
        """
        deletes all movie to genre records of given movie id.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2GenreEntity)\
            .filter(Movie2GenreEntity.movie_id == movie_id).delete()
