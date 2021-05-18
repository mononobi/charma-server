# -*- coding: utf-8 -*-
"""
movies related directors services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_persons.directors import RelatedDirectorsPackage


def get(movie_id, person_id):
    """
    gets movie to director with given ids.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :raises Movie2DirectorDoesNotExistError: movie 2 director does not exist error.

    :rtype: Movie2DirectorEntity
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).get(movie_id, person_id)


def create(movie_id, person_id, **options):
    """
    creates a new movie 2 director record.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :keyword bool is_main: is main.

    :raises ValidationError: validation error.
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).create(movie_id,
                                                                        person_id, **options)


def delete(movie_id, person_id, **options):
    """
    deletes a movie to director record.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :rtype: int
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).delete(movie_id,
                                                                        person_id, **options)


def delete_by_movie(movie_id, **options):
    """
    deletes all movie to director records of given movie id.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).delete_by_movie(movie_id,
                                                                                 **options)


def delete_by_director(person_id, **options):
    """
    deletes all movie to director records of given person id.

    it returns the count of deleted records.

    :param uuid.UUID person_id: person id.

    :rtype: int
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).delete_by_director(person_id,
                                                                                    **options)


def exists(movie_id, **options):
    """
    gets a value indicating that given movie has any directors.

    :param uuid.UUID movie_id: movie id.

    :rtype: bool
    """

    return get_component(RelatedDirectorsPackage.COMPONENT_NAME).exists(movie_id, **options)
