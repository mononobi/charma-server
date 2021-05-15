# -*- coding: utf-8 -*-
"""
movies manager module.
"""

import pyrin.globalization.datetime.services as datetime_services
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

        :rtype: imovie.movies.models.MovieEntity
        """

        store = get_current_store()
        return store.query(MovieEntity).get(id)

    def get(self, id):
        """
        gets movie with given id.

        it raises an error if movie does not exist.

        :param uuid.UUID id: movie id.

        :raises MovieDoesNotExistError: movie does not exist error.

        :rtype: imovie.movies.models.MovieEntity
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
        :keyword uuid.UUID content_rate_id: content rate id.
        :keyword int resolution: resolution.

        :returns: created movie id
        :rtype: uuid.UUID
        """

        options.update(library_title=library_title, directory_name=directory_name)
        validator_services.validate_dict(MovieEntity, options)
        entity = MovieEntity(**options)
        entity.search_library_title = self.get_normalized_name(entity.library_title)
        entity.search_title = self.get_normalized_name(entity.title)
        entity.search_original_title = self.get_normalized_name(entity.original_title)
        entity.search_storyline = self.get_normalized_name(entity.storyline)
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
        :keyword uuid.UUID content_rate_id: content rate id.
        :keyword int resolution: resolution.

        :raises ValidationError: validation error.
        :raises MovieDoesNotExistError: movie does not exist error.
        """

        validator_services.validate_dict(MovieEntity, options, for_update=True)
        entity = self.get(id)
        entity.update(**options)
        entity.search_library_title = self.get_normalized_name(entity.library_title)
        entity.search_title = self.get_normalized_name(entity.title)
        entity.search_original_title = self.get_normalized_name(entity.original_title)
        entity.search_storyline = self.get_normalized_name(entity.storyline)
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
        return store.query(MovieEntity).filter(MovieEntity.id == id).delete()

    def get_fullname(self, title, production_year, resolution, **options):
        """
        gets the movie fullname from given inputs.

        it returns the fullname with given format:
        title [production_year] [resolution]

        for example:
        Crash [2005] [720p]

        if the production year is None:
        Crash [720p]

        :param str title: movie title.
        :param int production_year: production year.

        :param int resolution: movie resolution.
        :enum resolution:
            UNKNOWN = 0
            VCD = 1
            DVD = 2
            HD = 3
            FHD = 4
            QHD = 5
            UHD = 6

        :rtype: str
        """

        result = '{title} [{year}] [{resolution}]'
        if production_year is None:
            result = '{title} [{resolution}]'

        resolution = MovieEntity.ResolutionEnum(resolution)
        return result.format(title=title, year=production_year, resolution=resolution)

    def get_full_title(self, title, production_year, **options):
        """
        gets the movie full title from given inputs.

        it returns full title with given format:
        title (production_year)

        for example:
        Crash (2005)

        if the production year is None:
        Crash

        :param str title: movie title.
        :param int production_year: production year.

        :rtype: str
        """

        result = '{title} ({year})'
        if production_year is None:
            result = '{title}'

        return result.format(title=title, year=production_year)

    def get_max_production_year(self):
        """
        gets the maximum acceptable production year for movies.

        :rtype: int
        """

        return datetime_services.current_year() + 1
