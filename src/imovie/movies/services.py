# -*- coding: utf-8 -*-
"""
movies services module.
"""

from pyrin.application.services import get_component

from imovie.movies import MoviesPackage


def get(id):
    """
    gets movie with given id.

    it raises an error if movie does not exist.

    :param uuid.UUID id: movie id.

    :raises MovieDoesNotExistError: movie does not exist error.

    :rtype: MovieEntity
    """

    return get_component(MoviesPackage.COMPONENT_NAME).get(id)


def create(library_title, directory_name, **options):
    """
    creates a new movie.

    :param str library_title: library title.
    :param str directory_name: directory name.

    :keyword str title: title.
    :keyword str original_title: original title.
    :keyword int production_year: production year.
    :keyword int | float imdb_rate: imdb rate.
    :keyword int meta_score: meta score.
    :keyword int runtime: runtime.
    :keyword str imdb_page: imdb page.
    :keyword str poster_name: poster name.
    :keyword str storyline: storyline.
    :keyword int content_rate: content_rate.
    :keyword int resolution: resolution.

    :returns: created movie id
    :rtype: uuid.UUID
    """

    return get_component(MoviesPackage.COMPONENT_NAME).create(library_title,
                                                              directory_name, **options)


def update(id, **options):
    """
    updates a movie with given id.

    :param uuid.UUID id: movie id.

    :keyword str library_title: library title.
    :keyword str directory_name: directory name.
    :keyword str title: title.
    :keyword str original_title: original title.
    :keyword int production_year: production year.
    :keyword int | float imdb_rate: imdb rate.
    :keyword int meta_score: meta score.
    :keyword int runtime: runtime.
    :keyword str imdb_page: imdb page.
    :keyword str poster_name: poster name.
    :keyword str storyline: storyline.
    :keyword int content_rate: content_rate.
    :keyword int resolution: resolution.

    :raises ValidationError: validation error.
    :raises MovieDoesNotExistError: movie does not exist error.
    """

    return get_component(MoviesPackage.COMPONENT_NAME).update(id, **options)


def delete(id):
    """
    deletes a movie with given id.

    :param uuid.UUID id: movie id.

    :returns: count of deleted items.
    :rtype: int
    """

    return get_component(MoviesPackage.COMPONENT_NAME).delete(id)


def find(**filters):
    """
    finds movies with given filters.

    :keyword str title: title.
    :keyword str original_title: original title.
    :keyword str library_title: library title.
    :keyword int production_year: production year.
    :keyword int from_production_year: from production year.
    :keyword int to_production_year: to production year.
    :keyword float | int imdb_rate: imdb rate.
    :keyword float | int from_imdb_rate: from imdb rate.
    :keyword float | int to_imdb_rate: to imdb rate.
    :keyword int meta_score: meta score.
    :keyword int from_meta_score: from meta score.
    :keyword int to_meta_score: to meta score.
    :keyword int from_runtime: from runtime.
    :keyword int to_runtime: to runtime.
    :keyword str imdb_page: imdb page.
    :keyword str poster_name: poster name.
    :keyword str directory_name: directory name.
    :keyword bool is_watched: is watched.
    :keyword str storyline: storyline.
    :keyword datetime from_watched_date: from watched date.
    :keyword datetime to_watched_date: to watched date.
    :keyword int | list[int] content_rate: content rate.
    :keyword int | list[int] resolution: resolution.
    :keyword datetime from_created_on: from created on.
    :keyword datetime to_created_on: to created on.

    :keyword bool consider_begin_of_day: specifies that consider begin
                                         of day for lower datetime.
                                         defaults to True if not provided.

    :keyword bool consider_end_of_day: specifies that consider end
                                       of day for upper datetime.
                                       defaults to True if not provided.

    :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                    to be used in select list.
                                                    if not provided, `MovieEntity`
                                                    will be used.

    :keyword list[str] | str order_by: order by columns.

    :rtype: list[MovieEntity]
    """

    return get_component(MoviesPackage.COMPONENT_NAME).find(**filters)


def exists(**options):
    """
    gets a value indicating that a movie exists.

    it searches using given imdb page link but if it
    fails, it searches with given title if provided.

    :keyword str imdb_page: imdb page link.
    :keyword str title: title.

    :rtype: bool
    """

    return get_component(MoviesPackage.COMPONENT_NAME).exists(**options)


def get_all(**options):
    """
    gets all movies.

    :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                    to be used in select list.
                                                    if not provided, `MovieEntity`
                                                    will be used.

    :keyword list[str] | str order_by: order by columns.

    :rtype: list[MovieEntity]
    """

    return get_component(MoviesPackage.COMPONENT_NAME).get_all(**options)


def try_get(**options):
    """
    gets a movie with given imdb page link or title.

    it searches using given imdb page link but if it
    fails, it searches with given title if provided.
    it returns None if movie not found.

    :keyword str imdb_page: imdb page link.
    :keyword str title: title.

    :rtype: MovieEntity
    """

    return get_component(MoviesPackage.COMPONENT_NAME).try_get(**options)
