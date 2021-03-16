# -*- coding: utf-8 -*-
"""
movies manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.movies import MoviesPackage
from imovie.movies.hooks import MovieHookBase
from imovie.movies.models import MovieEntity
from imovie.movies.queries import MoviesQueries
from imovie.movies.exceptions import MovieDoesNotExistError, InvalidMovieHookTypeError


class MoviesManager(Manager, MoviesQueries, HookMixin):
    """
    movies manager class.
    """

    package_class = MoviesPackage
    hook_type = MovieHookBase
    invalid_hook_type_error = InvalidMovieHookTypeError

    def _get(self, id):
        """
        gets movie with given id.

        it returns None if movie does not exist.

        :param uuid.UUID id: movie id.

        :rtype: MovieEntity
        """

        store = get_current_store()
        return store.query(MovieEntity).get(id)

    def get(self, id):
        """
        gets movie with given id.

        it raises an error if movie does not exist.

        :param uuid.UUID id: movie id.

        :raises MovieDoesNotExistError: movie does not exist error.

        :rtype: MovieEntity
        """

        entity = self._get(id)
        if entity is None:
            raise MovieDoesNotExistError(_('Movie with id [{id}] does not exist.')
                                         .format(id=id))
        return entity

    def create(self, library_title, directory_name, **options):
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

        options.update(library_title=library_title, directory_name=directory_name)
        validator_services.validate_dict(MovieEntity, options)
        entity = MovieEntity(**options)
        entity.search_library_title = self.get_normalized(entity.library_title)
        entity.identifier = self.get_normalized(entity.imdb_page)
        entity.search_title = self.get_normalized(entity.title)
        entity.search_original_title = self.get_normalized(entity.original_title)
        entity.search_storyline = self.get_normalized(entity.storyline)
        entity.save()

        return entity.id

    def update(self, id, **options):
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

        validator_services.validate_dict(MovieEntity, options, for_update=True)
        entity = self.get(id)
        entity.update(**options)
        entity.search_library_title = self.get_normalized(entity.library_title)
        entity.identifier = self.get_normalized(entity.imdb_page)
        entity.search_title = self.get_normalized(entity.title)
        entity.search_original_title = self.get_normalized(entity.original_title)
        entity.search_storyline = self.get_normalized(entity.storyline)
        entity.save()

    def delete(self, id):
        """
        deletes a movie with given id.

        :param uuid.UUID id: movie id.

        :returns: count of deleted items.
        :rtype: int
        """

        for hook in self._get_hooks():
            hook.before_delete(id)

        store = get_current_store()
        return store.query(MovieEntity.id).filter(MovieEntity.id == id).delete()
