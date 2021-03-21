# -*- coding: utf-8 -*-
"""
movies favorite manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from imovie.movies.models import FavoriteMovieEntity
from imovie.movies.favorite import FavoriteMoviesPackage
from imovie.movies.favorite.exceptions import FavoriteMovieDoesNotExistError


class FavoriteMoviesManager(Manager):
    """
    favorite movies manager class.
    """

    package_class = FavoriteMoviesPackage

    def _get(self, movie_id):
        """
        gets favorite movie with given id.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.

        :rtype: FavoriteMovieEntity
        """

        store = get_current_store()
        return store.query(FavoriteMovieEntity).get(movie_id)

    def get(self, movie_id):
        """
        gets favorite movie with given id.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.

        :raises FavoriteMovieDoesNotExistError: favorite movie does not exist error.

        :rtype: FavoriteMovieEntity
        """

        entity = self._get(movie_id)
        if entity is None:
            raise FavoriteMovieDoesNotExistError(_('Favorite movie with id '
                                                   '[{movie}] does not exist.')
                                                 .format(movie=movie_id))
        return entity

    def create(self, movie_id, favorite_rate, **options):
        """
        creates a new favorite movie.

        :param uuid.UUID movie_id: movie id.
        :param int favorite_rate: favorite rate.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, favorite_rate=favorite_rate, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(FavoriteMovieEntity, options)
        entity = FavoriteMovieEntity(**options)
        entity.save()

    def update(self, movie_id, favorite_rate, **options):
        """
        updates a favorite movie.

        :param uuid.UUID movie_id: movie id.
        :param int favorite_rate: favorite rate.

        :raises ValidationError: validation error.
        """

        options.update(favorite_rate=favorite_rate)
        validator_services.validate_dict(FavoriteMovieEntity, options, for_update=True)
        entity = self.get(movie_id)
        entity.update(**options)
        entity.save()

    def delete(self, movie_id, **options):
        """
        deletes a favorite movie.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(FavoriteMovieEntity.movie_id)\
            .filter(FavoriteMovieEntity.movie_id == movie_id).delete()
