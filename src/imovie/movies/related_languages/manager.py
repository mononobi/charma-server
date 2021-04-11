# -*- coding: utf-8 -*-
"""
movies related languages manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager
from pyrin.core.globals import _, SECURE_FALSE
from pyrin.database.services import get_current_store

from imovie.movies.models import Movie2LanguageEntity
from imovie.movies.related_languages import RelatedLanguagesPackage
from imovie.movies.related_languages.exceptions import Movie2LanguageDoesNotExistError


class RelatedLanguagesManager(Manager):
    """
    movies related languages manager class.
    """

    package_class = RelatedLanguagesPackage

    def _get(self, movie_id, language_id):
        """
        gets movie to language with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID language_id: language id.

        :rtype: Movie2LanguageEntity
        """

        store = get_current_store()
        return store.query(Movie2LanguageEntity).get((movie_id, language_id))

    def get(self, movie_id, language_id):
        """
        gets movie to language with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID language_id: language id.

        :raises Movie2LanguageDoesNotExistError: movie 2 language does not exist error.

        :rtype: Movie2LanguageEntity
        """

        entity = self._get(movie_id, language_id)
        if entity is None:
            raise Movie2LanguageDoesNotExistError(_('Movie to language with movie id '
                                                    '[{movie}] and language id [{language}] '
                                                    'does not exist.')
                                                  .format(movie=movie_id, language=language_id))
        return entity

    def create(self, movie_id, language_id, **options):
        """
        creates a new movie 2 language record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID language_id: language id.

        :keyword bool is_main: is main.

        :raises ValidationError: validation error.
        """

        options.update(movie_id=movie_id, language_id=language_id, ignore_pk=SECURE_FALSE)
        validator_services.validate_dict(Movie2LanguageEntity, options)
        entity = Movie2LanguageEntity(**options)
        entity.save()

    def delete(self, movie_id, language_id, **options):
        """
        deletes a movie to language record.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID language_id: language id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2LanguageEntity)\
            .filter(Movie2LanguageEntity.movie_id == movie_id,
                    Movie2LanguageEntity.language_id == language_id).delete()

    def delete_by_movie(self, movie_id, **options):
        """
        deletes all movie to language records of given movie id.

        it returns the count of deleted records.

        :param uuid.UUID movie_id: movie id.

        :rtype: int
        """

        store = get_current_store()
        return store.query(Movie2LanguageEntity)\
            .filter(Movie2LanguageEntity.movie_id == movie_id).delete()
