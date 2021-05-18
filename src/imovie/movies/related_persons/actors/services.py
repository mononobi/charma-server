# -*- coding: utf-8 -*-
"""
movies related actors services module.
"""

from pyrin.application.services import get_component

from imovie.movies.related_persons.actors import RelatedActorsPackage


def get(movie_id, person_id):
    """
    gets movie to actor with given ids.

    it raises an error if it does not exist.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :raises Movie2ActorDoesNotExistError: movie 2 actor does not exist error.

    :rtype: Movie2ActorEntity
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).get(movie_id, person_id)


def create(movie_id, person_id, **options):
    """
    creates a new movie 2 actor record.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :keyword bool is_star: is star.
    :keyword str character: character name.

    :raises ValidationError: validation error.
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).create(movie_id,
                                                                     person_id, **options)


def delete(movie_id, person_id, **options):
    """
    deletes a movie to actor record.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.
    :param uuid.UUID person_id: person id.

    :rtype: int
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).delete(movie_id,
                                                                     person_id, **options)


def delete_by_movie(movie_id, **options):
    """
    deletes all movie to actor records of given movie id.

    it returns the count of deleted records.

    :param uuid.UUID movie_id: movie id.

    :rtype: int
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).delete_by_movie(movie_id,
                                                                              **options)


def delete_by_actor(person_id, **options):
    """
    deletes all movie to actor records of given person id.

    it returns the count of deleted records.

    :param uuid.UUID person_id: person id.

    :rtype: int
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).delete_by_actor(person_id,
                                                                              **options)


def exists(movie_id, **options):
    """
    gets a value indicating that given movie has any actors.

    :param uuid.UUID movie_id: movie id.

    :rtype: bool
    """

    return get_component(RelatedActorsPackage.COMPONENT_NAME).exists(movie_id, **options)
