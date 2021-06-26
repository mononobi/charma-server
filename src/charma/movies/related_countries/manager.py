# -*- coding: utf-8 -*-
"""
movies related countries manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from charma.movies.models import Movie2CountryEntity
from charma.movies.related_countries import RelatedCountriesPackage
from charma.movies.related_countries.exceptions import Movie2CountryDoesNotExistError


class RelatedCountriesManager(Manager):
    """
    movies related countries manager class.
    """

    package_class = RelatedCountriesPackage

    def _get(self, movie_id, country_id):
        """
        gets movie to country with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID country_id: country id.

        :rtype: Movie2CountryEntity
        """

        store = get_current_store()
        return store.query(Movie2CountryEntity).get((movie_id, country_id))

    def get(self, movie_id, country_id):
        """
        gets movie to country with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID country_id: country id.

        :raises Movie2CountryDoesNotExistError: movie 2 country does not exist error.

        :rtype: Movie2CountryEntity
        """

        entity = self._get(movie_id, country_id)
        if entity is None:
            raise Movie2CountryDoesNotExistError(_('Movie to country with movie id '
                                                   '[{movie}] and country id [{country}] '
                                                   'does not exist.')
                                                 .format(movie=movie_id, country=country_id))
        return entity

    def create(self, movie_id, country_id, **options):
        """
        creates a new movie 2 country record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID country_id: country id.

        :keyword bool is_main: is main.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, country_id=country_id, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(Movie2CountryEntity, options)
        entity = Movie2CountryEntity(**options)
        entity.save()

    def delete(self, movie_id, country_id, **options):
        """
        deletes a movie to country record.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID country_id: country id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2CountryEntity)\
            .filter(Movie2CountryEntity.movie_id == movie_id,
                    Movie2CountryEntity.country_id == country_id).delete()

    def delete_by_movie(self, movie_id, **options):
        """
        deletes all movie to country records of given movie id.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2CountryEntity)\
            .filter(Movie2CountryEntity.movie_id == movie_id).delete()

    def exists(self, movie_id, **options):
        """
        gets a value indicating that given movie has any countries.

        :param uuid.UUID movie_id: movie id.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(Movie2CountryEntity.movie_id)\
            .filter(Movie2CountryEntity.movie_id == movie_id).existed()
