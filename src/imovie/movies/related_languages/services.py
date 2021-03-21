# -*- coding: utf-8 -*-
"""
movies related languages services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_languages import RelatedLanguagesPackage


def get(movie_id, language_id):
    """
    gets movie to language with given ids.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID language_id: language id.

    :raises Movie2LanguageDoesNotExistError: movie 2 language does not exist error.

    :rtype: Movie2LanguageEntity
    """

    return get_component(RelatedLanguagesPackage.COMPONENT_NAME).get(movie_id, language_id)


def create(movie_id, language_id, **options):
    """
    creates a new movie 2 language record.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID language_id: language id.

    :keyword bool is_main: is main.

    :raises ValidationError: validation error.
    """

    return get_component(RelatedLanguagesPackage.COMPONENT_NAME).create(movie_id,
                                                                        language_id, **options)


def delete(movie_id, language_id, **options):
    """
    deletes a movie to language record.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID language_id: language id.

    :rtype: int
    """

    return get_component(RelatedLanguagesPackage.COMPONENT_NAME).delete(movie_id,
                                                                        language_id, **options)


def delete_by_movie(movie_id, **options):
    """
    deletes all movie to language records of given movie id.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(RelatedLanguagesPackage.COMPONENT_NAME).delete_by_movie(movie_id,
                                                                                 **options)
