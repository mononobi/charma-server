# -*- coding: utf-8 -*-
"""
movies queries module.
"""

from sqlalchemy import or_

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.globals import SECURE_TRUE
from pyrin.core.structs import CoreObject
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import add_datetime_range_clause, add_range_clause
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

from imovie.movies.models import MovieEntity


class MoviesQueries(CoreObject):
    """
    movies queries class.
    """

    NAME_NORMALIZERS = [NormalizerEnum.PERSIAN_SIGN,
                        NormalizerEnum.LATIN_SIGN,
                        NormalizerEnum.PERSIAN_NUMBER,
                        NormalizerEnum.ARABIC_NUMBER,
                        NormalizerEnum.PERSIAN_LETTER,
                        NormalizerEnum.LATIN_LETTER,
                        NormalizerEnum.LOWERCASE,
                        NormalizerEnum.SPACE]

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

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

        :rtype: list
        """

        title = filters.get('title')
        original_title = filters.get('original_title')
        library_title = filters.get('library_title')
        production_year = filters.get('production_year')
        from_production_year = filters.get('from_production_year')
        to_production_year = filters.get('to_production_year')
        imdb_rate = filters.get('imdb_rate')
        from_imdb_rate = filters.get('from_imdb_rate')
        to_imdb_rate = filters.get('to_imdb_rate')
        meta_score = filters.get('meta_score')
        from_meta_score = filters.get('from_meta_score')
        to_meta_score = filters.get('to_meta_score')
        from_runtime = filters.get('from_runtime')
        to_runtime = filters.get('to_runtime')
        imdb_page = filters.get('imdb_page')
        poster_name = filters.get('poster_name')
        directory_name = filters.get('directory_name')
        is_watched = filters.get('is_watched')
        storyline = filters.get('storyline')
        from_watched_date = filters.get('from_watched_date')
        to_watched_date = filters.get('to_watched_date')
        content_rate = filters.get('content_rate')
        resolution = filters.get('resolution')
        from_created_on = filters.get('from_created_on')
        to_created_on = filters.get('to_created_on')

        if title is not None:
            search_title = self._get_normalized(title)
            expressions.append(MovieEntity.search_title.icontains(search_title))

        if original_title is not None:
            search_original_title = self._get_normalized(original_title)
            expressions.append(MovieEntity.search_original_title.icontains(search_original_title))

        if library_title is not None:
            search_library_title = self._get_normalized(library_title)
            expressions.append(MovieEntity.search_library_title.icontains(search_library_title))

        if production_year is not None:
            expressions.append(MovieEntity.production_year == production_year)

        if from_production_year is not None or to_production_year is not None:
            add_range_clause(expressions, MovieEntity.production_year,
                             from_production_year, to_production_year, **filters)

        if imdb_rate is not None:
            expressions.append(MovieEntity.imdb_rate == imdb_rate)

        if from_imdb_rate is not None or to_imdb_rate is not None:
            add_range_clause(expressions, MovieEntity.imdb_rate,
                             from_imdb_rate, to_imdb_rate, **filters)

        if meta_score is not None:
            expressions.append(MovieEntity.meta_score == meta_score)

        if from_meta_score is not None or to_meta_score is not None:
            add_range_clause(expressions, MovieEntity.meta_score,
                             from_meta_score, to_meta_score, **filters)

        if from_runtime is not None or to_runtime is not None:
            add_range_clause(expressions, MovieEntity.runtime,
                             from_runtime, to_runtime, **filters)

        if imdb_page is not None:
            identifier = self._get_normalized(imdb_page)
            expressions.append(MovieEntity.identifier.icontains(identifier))

        if poster_name is not None:
            expressions.append(MovieEntity.poster_name.icontains(poster_name))

        if directory_name is not None:
            expressions.append(MovieEntity.directory_name.icontains(directory_name))

        if is_watched is not None:
            expressions.append(MovieEntity.is_watched == is_watched)

        if storyline is not None:
            search_storyline = self._get_normalized(storyline)
            expressions.append(MovieEntity.search_storyline.icontains(search_storyline))

        if from_watched_date is not None or to_watched_date is not None:
            add_datetime_range_clause(expressions, MovieEntity.watched_date,
                                      from_watched_date, to_watched_date, **filters)

        if content_rate is not None:
            expressions.append(MovieEntity.content_rate.in_(content_rate))

        if resolution is not None:
            expressions.append(MovieEntity.resolution.in_(resolution))

        if from_created_on is not None or to_created_on is not None:
            add_datetime_range_clause(expressions, MovieEntity.created_on,
                                      from_created_on, to_created_on, **filters)

    def _get_normalized(self, value):
        """
        gets normalized value from given value.

        :param str value: value to be normalized.

        :rtype: str
        """

        return normalizer_services.normalize(value, *self.NAME_NORMALIZERS)

    def _get_all(self, *expressions, **options):
        """
        gets all movies using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `MovieEntity`
                                                        will be used.

        :rtype: list[MovieEntity]
        """

        columns = options.get('columns') or [MovieEntity]
        store = get_current_store()
        query = store.query(*columns)
        query = self._prepare_query(query)

        return query.filter(*expressions).paginate(inject_total=SECURE_TRUE, **options).all()

    def _prepare_query(self, query):
        """
        prepares given query object.

        this method is intended to overridden in subclasses to
        limit results to specific movie type using join.
        for example to only get duplicate movies or favorite movies or ...

        :param CoreQuery query: query object to be prepared.

        :rtype: CoreQuery
        """

        return query

    def _exists_by_imdb_page(self, imdb_page, **options):
        """
        gets a value indicating a movie with given imdb page exists.

        :param str imdb_page: imdb page link.

        :rtype: bool
        """

        if imdb_page in (None, ''):
            return False

        identifier = self._get_normalized(imdb_page)
        store = get_current_store()
        query = store.query(MovieEntity.id)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.identifier.ilike(identifier)).existed()

    def _exists_by_title(self, title, **options):
        """
        gets a value indicating a movie with given title exists.

        it only returns True if found movie has no imdb page link.

        :param str title: title.

        :rtype: bool
        """

        if title in (None, ''):
            return False

        search_title = self._get_normalized(title)
        store = get_current_store()
        query = store.query(MovieEntity.id)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.search_title.ilike(search_title),
                            or_(MovieEntity.imdb_page is None,
                                MovieEntity.imdb_page == '')).existed()

    def _get_by_imdb_page(self, imdb_page, **options):
        """
        gets a movie by its imdb page link.

        it returns None if movie not found.

        :param str imdb_page: imdb page link.

        :rtype: MovieEntity
        """

        identifier = self._get_normalized(imdb_page)
        store = get_current_store()
        query = store.query(MovieEntity)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.identifier.ilike(identifier)).one_or_none()

    def _get_by_title(self, title, **options):
        """
        gets a movie by its title.

        it returns None if movie not found.
        it only returns if found movie has no imdb page link.

        :param str title: title.

        :rtype: MovieEntity
        """

        search_title = self._get_normalized(title)
        store = get_current_store()
        query = store.query(MovieEntity)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.search_title.ilike(search_title),
                            or_(MovieEntity.imdb_page is None,
                                MovieEntity.imdb_page == '')).first()

    def find(self, **filters):
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

        :rtype: list[MovieEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions, **filters)

    def exists(self, **options):
        """
        gets a value indicating that a movie exists.

        it searches using given imdb page link but if it
        fails, it searches with given title if provided.

        :keyword str imdb_page: imdb page link.
        :keyword str title: title.

        :rtype: bool
        """

        imdb_page = options.pop('imdb_page', None)
        existed = self._exists_by_imdb_page(imdb_page, **options)
        if existed is False:
            title = options.pop('title', None)
            existed = self._exists_by_title(title, **options)

        return existed

    def get_all(self, **options):
        """
        gets all movies.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `MovieEntity`
                                                        will be used.

        :rtype: list[MovieEntity]
        """

        return self._get_all(**options)

    def try_get(self, **options):
        """
        gets a movie with given imdb page link or title.

        it searches using given imdb page link but if it
        fails, it searches with given title if provided.
        it returns None if movie not found.

        :keyword str imdb_page: imdb page link.
        :keyword str title: title.

        :rtype: MovieEntity
        """

        imdb_page = options.pop('imdb_page', None)
        entity = self._get_by_imdb_page(imdb_page, **options)
        if entity is None:
            title = options.pop('title', None)
            entity = self._get_by_title(title, **options)

        return entity