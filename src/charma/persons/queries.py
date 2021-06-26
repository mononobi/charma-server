# -*- coding: utf-8 -*-
"""
persons queries module.
"""

from sqlalchemy import or_

import pyrin.validator.services as validator_services

from pyrin.core.globals import SECURE_TRUE
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import add_datetime_range_clause

from charma.common.normalizer.mixin import NormalizerMixin
from charma.persons.models import PersonEntity


class PersonsQueries(NormalizerMixin):
    """
    persons queries class.
    """

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str fullname: fullname.
        :keyword str imdb_page: imdb page link.
        :keyword str photo_name: photo file name.
        :keyword datetime from_created_on: from created on.
        :keyword datetime to_created_on: to created on.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to False if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to False if not provided.

        :rtype: list
        """

        validator_services.validate_for_find(PersonEntity, filters)

        fullname = filters.get('fullname')
        imdb_page = filters.get('imdb_page')
        photo_name = filters.get('photo_name')
        from_created_on = filters.get('from_created_on')
        to_created_on = filters.get('to_created_on')

        if fullname is not None:
            search_name = self.get_normalized_name(fullname)
            expressions.append(PersonEntity.search_name.icontains(search_name))

        if imdb_page is not None:
            expressions.append(PersonEntity.imdb_page.icontains(imdb_page))

        if photo_name is not None:
            expressions.append(PersonEntity.photo_name.icontains(photo_name))

        if from_created_on is not None or to_created_on is not None:
            add_datetime_range_clause(expressions, PersonEntity.created_on,
                                      from_created_on, to_created_on, **filters)

    def _get_all(self, *expressions, **options):
        """
        gets all persons using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

        :rtype: list[PersonEntity]
        """

        columns = options.get('columns') or [PersonEntity]
        store = get_current_store()
        query = store.query(*columns)
        query = self._prepare_query(query)
        options.update(inject_total=SECURE_TRUE)

        return query.filter(*expressions)\
            .safe_order_by(PersonEntity, 'created_on', **options)\
            .paginate(**options).all()

    def _prepare_query(self, query):
        """
        prepares given query object.

        this method is intended to overridden in subclasses to
        limit results to specific person type using join.

        :param CoreQuery query: query object to be prepared.

        :rtype: CoreQuery
        """

        return query

    def _exists_by_imdb_page(self, imdb_page, **options):
        """
        gets a value indicating a person with given imdb page exists.

        :param str imdb_page: imdb page link.

        :rtype: bool
        """

        if imdb_page in (None, ''):
            return False

        store = get_current_store()
        query = store.query(PersonEntity.id)
        query = self._prepare_query(query)

        return query.filter(PersonEntity.imdb_page.ilike(imdb_page)).existed()

    def _exists_by_fullname(self, fullname, **options):
        """
        gets a value indicating a person with given fullname exists.

        it only returns True if found person has no imdb page link.

        :param str fullname: fullname.

        :rtype: bool
        """

        if fullname in (None, ''):
            return False

        search_name = self.get_normalized_name(fullname)
        store = get_current_store()
        query = store.query(PersonEntity.id)
        query = self._prepare_query(query)

        return query.filter(PersonEntity.search_name.ilike(search_name),
                            or_(PersonEntity.imdb_page == None,
                                PersonEntity.imdb_page == '')).existed()

    def _get_by_imdb_page(self, imdb_page, **options):
        """
        gets a person by its imdb page link.

        it returns None if person not found.

        :param str imdb_page: imdb page link.

        :rtype: PersonEntity
        """

        store = get_current_store()
        query = store.query(PersonEntity)
        query = self._prepare_query(query)

        return query.filter(PersonEntity.imdb_page.ilike(imdb_page)).one_or_none()

    def _get_by_fullname(self, fullname, **options):
        """
        gets a person by its fullname.

        it returns None if person not found.
        it only returns if found person has no imdb page link.

        :param str fullname: fullname.

        :rtype: PersonEntity
        """

        search_name = self.get_normalized_name(fullname)
        store = get_current_store()
        query = store.query(PersonEntity)
        query = self._prepare_query(query)

        return query.filter(PersonEntity.search_name.ilike(search_name),
                            or_(PersonEntity.imdb_page == None,
                                PersonEntity.imdb_page == '')).first()

    def find(self, **filters):
        """
        finds persons with given filters.

        :keyword str fullname: fullname.
        :keyword str imdb_page: imdb page link.
        :keyword str photo_name: photo file name.
        :keyword datetime from_created_on: from created on.
        :keyword datetime to_created_on: to created on.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to False if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to False if not provided.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

        :rtype: list[PersonEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions, **filters)

    def exists(self, **options):
        """
        gets a value indicating that a person exists.

        it searches using given imdb page link but if it
        fails, it searches with given name if provided.

        :keyword str imdb_page: imdb page link.
        :keyword str fullname: fullname.

        :rtype: bool
        """

        imdb_page = options.pop('imdb_page', None)
        existed = self._exists_by_imdb_page(imdb_page, **options)
        if existed is False:
            fullname = options.pop('fullname', None)
            existed = self._exists_by_fullname(fullname, **options)

        return existed

    def get_all(self, **options):
        """
        gets all persons.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[str] | str order_by: order by columns.

        :rtype: list[PersonEntity]
        """

        return self._get_all(**options)

    def try_get(self, **options):
        """
        gets a person with given imdb page link or fullname.

        it searches using given imdb page link but if it
        fails, it searches with given name if provided.
        it returns None if person not found.

        :keyword str imdb_page: imdb page link.
        :keyword str fullname: fullname.

        :rtype: PersonEntity
        """

        imdb_page = options.pop('imdb_page', None)
        entity = self._get_by_imdb_page(imdb_page, **options)
        if entity is None:
            fullname = options.pop('fullname', None)
            entity = self._get_by_fullname(fullname, **options)

        return entity
