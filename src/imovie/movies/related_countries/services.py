# -*- coding: utf-8 -*-
"""
movies related countries services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_countries import RelatedCountriesPackage


def get(movie_id, country_id):
    """
    gets movie to country with given ids.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID country_id: country id.

    :raises Movie2CountryDoesNotExistError: movie 2 country does not exist error.

    :rtype: Movie2CountryEntity
    """

    return get_component(RelatedCountriesPackage.COMPONENT_NAME).get(movie_id, country_id)


def create(movie_id, country_id, **options):
    """
    creates a new movie 2 country record.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID country_id: country id.

    :keyword bool is_main: is main.

    :raises ValidationError: validation error.
    """

    return get_component(RelatedCountriesPackage.COMPONENT_NAME).create(movie_id,
                                                                        country_id, **options)


def delete(movie_id, country_id, **options):
    """
    deletes a movie to country record.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID country_id: country id.

    :rtype: int
    """

    return get_component(RelatedCountriesPackage.COMPONENT_NAME).delete(movie_id,
                                                                        country_id, **options)


def delete_by_movie(movie_id, **options):
    """
    deletes all movie to country records of given movie id.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(RelatedCountriesPackage.COMPONENT_NAME).delete_by_movie(movie_id,
                                                                                 **options)
