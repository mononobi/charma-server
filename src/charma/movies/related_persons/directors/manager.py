# -*- coding: utf-8 -*-
"""
movies related directors manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from charma.movies.models import Movie2DirectorEntity
from charma.movies.related_persons.directors import RelatedDirectorsPackage
from charma.movies.related_persons.directors.exceptions import Movie2DirectorDoesNotExistError


class RelatedDirectorsManager(Manager):
    """
    movies related directors manager class.
    """

    package_class = RelatedDirectorsPackage

    def _get(self, movie_id, person_id):
        """
        gets movie to director with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :rtype: Movie2DirectorEntity
        """

        store = get_current_store()
        return store.query(Movie2DirectorEntity).get((movie_id, person_id))

    def get(self, movie_id, person_id):
        """
        gets movie to director with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :raises Movie2DirectorDoesNotExistError: movie 2 director does not exist error.

        :rtype: Movie2DirectorEntity
        """

        entity = self._get(movie_id, person_id)
        if entity is None:
            raise Movie2DirectorDoesNotExistError(_('Movie to director with movie id [{movie}] '
                                                    'and director id [{person}] does not exist.')
                                                  .format(movie=movie_id, person=person_id))
        return entity

    def create(self, movie_id, person_id, **options):
        """
        creates a new movie 2 director record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :keyword bool is_main: is_main.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, person_id=person_id, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(Movie2DirectorEntity, options)
        entity = Movie2DirectorEntity(**options)
        entity.save()

    def delete(self, movie_id, person_id, **options):
        """
        deletes a movie to director record.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2DirectorEntity)\
            .filter(Movie2DirectorEntity.movie_id == movie_id,
                    Movie2DirectorEntity.person_id == person_id).delete()

    def delete_by_movie(self, movie_id, **options):
        """
        deletes all movie to director records of given movie id.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2DirectorEntity)\
            .filter(Movie2DirectorEntity.movie_id == movie_id).delete()

    def delete_by_director(self, person_id, **options):
        """
        deletes all movie to director records of given person id.

        it returns the count of deleted records.

        :param uuid.UUID person_id: person id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2DirectorEntity)\
            .filter(Movie2DirectorEntity.person_id == person_id).delete()

    def exists(self, movie_id, **options):
        """
        gets a value indicating that given movie has any directors.

        :param uuid.UUID movie_id: movie id.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(Movie2DirectorEntity.movie_id)\
            .filter(Movie2DirectorEntity.movie_id == movie_id).existed()
