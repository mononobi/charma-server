# -*- coding: utf-8 -*-
"""
movies related actors manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from imovie.common.normalizer.mixin import NormalizerMixin
from imovie.movies.models import Movie2ActorEntity
from imovie.movies.related_persons.actors import RelatedActorsPackage
from imovie.movies.related_persons.actors.exceptions import Movie2ActorDoesNotExistError


class RelatedActorsManager(Manager, NormalizerMixin):
    """
    movies related actors manager class.
    """

    package_class = RelatedActorsPackage

    def _get(self, movie_id, person_id):
        """
        gets movie to actor with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :rtype: Movie2ActorEntity
        """

        store = get_current_store()
        return store.query(Movie2ActorEntity).get((movie_id, person_id))

    def get(self, movie_id, person_id):
        """
        gets movie to actor with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :raises Movie2ActorDoesNotExistError: movie 2 actor does not exist error.

        :rtype: Movie2ActorEntity
        """

        entity = self._get(movie_id, person_id)
        if entity is None:
            raise Movie2ActorDoesNotExistError(_('Movie to actor with movie id [{movie}] '
                                                 'and actor id [{person}] does not exist.')
                                               .format(movie=movie_id, person=person_id))
        return entity

    def create(self, movie_id, person_id, **options):
        """
        creates a new movie 2 actor record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :keyword bool is_star: is star.
        :keyword str character: character name.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, person_id=person_id, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(Movie2ActorEntity, options)
        entity = Movie2ActorEntity(**options)
        entity.search_character = self.get_normalized_name(entity.character)
        entity.save()

    def delete(self, movie_id, person_id, **options):
        """
        deletes a movie to actor record.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2ActorEntity.person_id)\
            .filter(Movie2ActorEntity.movie_id == movie_id,
                    Movie2ActorEntity.person_id == person_id).delete()

    def delete_by_movie(self, movie_id, **options):
        """
        deletes all movie to actor records of given movie id.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2ActorEntity.person_id)\
            .filter(Movie2ActorEntity.movie_id == movie_id).delete()

    def delete_by_actor(self, person_id, **options):
        """
        deletes all movie to actor records of given person id.

        it returns the count of deleted records.

        :param uuid.UUID person_id: person id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2ActorEntity.person_id)\
            .filter(Movie2ActorEntity.person_id == person_id).delete()
