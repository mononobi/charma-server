# -*- coding: utf-8 -*-
"""
movies manager module.
"""

from pyrin.core.context import CoreObject
from pyrin.database.services import get_current_store
from pyrin.utils.paging import extract_limit
from pyrin.utils.sqlalchemy import add_like_clause, add_list_clause, add_range_clause, \
    add_date_range_clause, entity_to_dict_list

from imovie.movies.models import MovieEntity


class MoviesManager(CoreObject):
    """
    movies manager class.
    """

    def _make_find_clause(self, **filters):
        """
        """

        clauses = []

        name = filters.get('name', None)
        release_year = filters.get('release_year', None)
        release_year_lower = filters.get('release_year_lower', None)
        release_year_upper = filters.get('release_year_upper', None)
        archive_date = filters.get('archive_date', None)
        archive_date_lower = filters.get('archive_date_lower', None)
        archive_date_upper = filters.get('archive_date_upper', None)
        imdb_rate = filters.get('imdb_rate', None)
        imdb_rate_lower = filters.get('imdb_rate_lower', None)
        imdb_rate_upper = filters.get('imdb_rate_upper', None)

        if name is not None:
            add_like_clause(clauses, MovieEntity.name, name)

        if release_year is not None:
            add_list_clause(clauses, MovieEntity.release_year, release_year)

        if release_year_lower is not None or release_year_upper is not None:
            add_range_clause(clauses, MovieEntity.release_year,
                             release_year_lower, release_year_upper)

        if archive_date is not None:
            add_date_range_clause(clauses, MovieEntity.archive_date,
                                  archive_date, archive_date)

        if archive_date_lower is not None or archive_date_upper is not None:
            add_date_range_clause(clauses, MovieEntity.archive_date,
                                  archive_date_lower, archive_date_upper, **filters)

        if imdb_rate is not None:
            clauses.append(MovieEntity.imdb_rate == imdb_rate)

        if imdb_rate_lower is not None or imdb_rate_upper is not None:
            add_range_clause(clauses, MovieEntity.imdb_rate,
                             imdb_rate_lower, imdb_rate_upper)

        return clauses

    def _find(self, *columns, **filters):
        """
        """

        clauses = self._make_find_clause(**filters)
        required_columns = (MovieEntity,)
        scope = None
        limit = extract_limit(filters)

        if len(columns) > 0:
            required_columns = columns
            scope = MovieEntity

        store = get_current_store()
        entities = store.query(*required_columns,
                               scope=scope).filter(*clauses).limit(limit).all()

        return entities

    def find(self, **filters):
        """
        """

        entities = self._find(**filters)

        return entity_to_dict_list(entities)
