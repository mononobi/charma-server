# -*- coding: utf-8 -*-
"""
movies queries module.
"""

from sqlalchemy import and_, or_

import pyrin.validator.services as validator_services
import pyrin.filtering.services as filtering_services

from pyrin.core.globals import SECURE_TRUE
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import add_datetime_range_clause

from charma.common.normalizer.mixin import NormalizerMixin
from charma.movies.models import MovieEntity, ContentRateEntity


class MoviesQueries(NormalizerMixin):
    """
    movies queries class.
    """

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
        :keyword uuid.UUID | list[uuid.UUID] content_rate_id: content rate id.
        :keyword int | list[int] resolution: resolution.
        :keyword datetime from_created_on: from created on.
        :keyword datetime to_created_on: to created on.
        :keyword datetime from_modified_on: from modified on.
        :keyword datetime to_modified_on: to modified on.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to False if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to False if not provided.

        :rtype: list
        """

        validator_services.validate_for_find(MovieEntity, filters)

        title = filters.pop('title', None)
        original_title = filters.pop('original_title', None)
        library_title = filters.pop('library_title', None)
        storyline = filters.pop('storyline', None)
        from_modified_on = filters.get('from_modified_on')
        to_modified_on = filters.get('to_modified_on')

        if title is not None:
            search_title = self.get_normalized_name(title)
            filters.update(search_title=search_title)

        if original_title is not None:
            search_original_title = self.get_normalized_name(original_title)
            filters.update(search_original_title=search_original_title)

        if library_title is not None:
            search_library_title = self.get_normalized_name(library_title)
            filters.update(search_library_title=search_library_title)

        if storyline is not None:
            search_storyline = self.get_normalized_name(storyline)
            filters.update(search_storyline=search_storyline)

        auto_expressions = filtering_services.filter(MovieEntity, filters,
                                                     MovieEntity.modified_on)
        expressions.extend(auto_expressions)

        if from_modified_on is not None or to_modified_on is not None:
            modified_on_range = []
            add_datetime_range_clause(modified_on_range, MovieEntity.modified_on,
                                      from_modified_on, to_modified_on, **filters)
            expressions.append(or_(and_(*modified_on_range), MovieEntity.modified_on == None))

    def _get_all(self, *expressions, **options):
        """
        gets all movies using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `MovieEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

        :rtype: list[MovieEntity]
        """

        columns = options.get('columns') or [MovieEntity,
                                             ContentRateEntity.name.label('content_rate')]
        store = get_current_store()
        query = store.query(*columns)
        query = query.outerjoin(ContentRateEntity,
                                ContentRateEntity.id == MovieEntity.content_rate_id)
        query = self._prepare_query(query)
        options.update(inject_total=SECURE_TRUE)

        return query.filter(*expressions)\
            .safe_order_by(MovieEntity, '-created_on', **options)\
            .paginate(**options).all()

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

        store = get_current_store()
        query = store.query(MovieEntity.id)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.imdb_page.ilike(imdb_page)).existed()

    def _exists_by_title(self, title, **options):
        """
        gets a value indicating a movie with given title exists.

        it only returns True if found movie has no imdb page link.

        :param str title: title.

        :rtype: bool
        """

        if title in (None, ''):
            return False

        search_title = self.get_normalized_name(title)
        store = get_current_store()
        query = store.query(MovieEntity.id)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.search_title.ilike(search_title),
                            or_(MovieEntity.imdb_page == None,
                                MovieEntity.imdb_page == '')).existed()

    def _get_by_imdb_page(self, imdb_page, **options):
        """
        gets a movie by its imdb page link.

        it returns None if movie not found.

        :param str imdb_page: imdb page link.

        :rtype: MovieEntity
        """

        store = get_current_store()
        query = store.query(MovieEntity)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.imdb_page.ilike(imdb_page)).one_or_none()

    def _get_by_title(self, title, **options):
        """
        gets a movie by its title.

        it returns None if movie not found.
        it only returns if found movie has no imdb page link.

        :param str title: title.

        :rtype: MovieEntity
        """

        search_title = self.get_normalized_name(title)
        store = get_current_store()
        query = store.query(MovieEntity)
        query = self._prepare_query(query)

        return query.filter(MovieEntity.search_title.ilike(search_title),
                            or_(MovieEntity.imdb_page == None,
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
        :keyword uuid.UUID | list[uuid.UUID] content_rate_id: content rate id.
        :keyword int | list[int] resolution: resolution.
        :keyword datetime from_created_on: from created on.
        :keyword datetime to_created_on: to created on.
        :keyword datetime from_modified_on: from modified on.
        :keyword datetime to_modified_on: to modified on.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to False if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to False if not provided.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `MovieEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

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

    def exists_by_directory(self, directory, **options):
        """
        gets a value indicating that a movie with given directory name exists.

        :param str directory: directory name.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(MovieEntity.id)\
            .filter(MovieEntity.directory_name.ilike(directory))\
            .existed()

    def get_all(self, **options):
        """
        gets all movies.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `MovieEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

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
