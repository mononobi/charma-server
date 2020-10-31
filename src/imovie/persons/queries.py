# -*- coding: utf-8 -*-
"""
persons queries module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.structs import CoreObject
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import add_datetime_range_clause
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

from imovie.persons.models import PersonEntity


class PersonsQueries(CoreObject):
    """
    persons queries class.
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

        :keyword str first_name: first name.
        :keyword str last_name: last name
        :keyword str imdb_page: imdb page link
        :keyword str photo_name: photo file name.
        :keyword datetime from_add_date: from add date.
        :keyword datetime to_add_date: to add date.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to True if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to True if not provided.

        :rtype: list
        """

        first_name = filters.get('first_name')
        last_name = filters.get('last_name')
        imdb_page = filters.get('imdb_page')
        photo_name = filters.get('photo_name')
        from_add_date = filters.get('from_add_date')
        to_add_date = filters.get('to_add_date')

        if first_name is not None or last_name is not None:
            search_name = self._get_search_name(first_name, last_name)
            expressions.append(PersonEntity.search_name.icontains(search_name))

        if imdb_page is not None:
            expressions.append(PersonEntity.imdb_page.icontains(imdb_page))

        if photo_name is not None:
            expressions.append(PersonEntity.photo_name.icontains(photo_name))

        if from_add_date is not None or to_add_date is not None:
            add_datetime_range_clause(expressions, PersonEntity.add_date,
                                      from_add_date, to_add_date, **filters)

    def _get_search_name(self, first_name, last_name):
        """
        gets search name from given inputs.

        :param str first_name: first name.
        :param str last_name: last name.

        :rtype: str
        """

        fullname = self.get_fullname(first_name, last_name)
        return normalizer_services.normalize(fullname, *self.NAME_NORMALIZERS)

    def _get_all(self, *expressions, **options):
        """
        gets all persons using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[tuple] joins: list of all join expressions to be performed on query.
                                    defaults to no join if not provided.
                                    values must be provided as a list of tuples.
                                    for example:
                                    joins=[(ActorEntity,
                                            ActorEntity.person_id == PersonEntity.id),
                                           (DirectorEntity,
                                            DirectorEntity.person_id == PersonEntity.id)]

        :rtype: list[PersonEntity]
        """

        joins = options.get('joins')
        columns = options.get('columns') or [PersonEntity]
        store = get_current_store()
        query = store.query(*columns)
        if joins is not None:
            for entity, criteria in joins:
                query = query.join(entity, criteria)

        return query.filter(*expressions).all()

    def get_fullname(self, first_name, last_name):
        """
        gets full name from given inputs.

        :param str first_name: first name.
        :param str last_name: last name.

        :rtype: str
        """

        has_first_name = first_name not in (None, '') and not first_name.isspace()
        has_last_name = last_name not in (None, '') and not last_name.isspace()

        if has_first_name is True and has_last_name is True:
            return '{first} {last}'.format(first=first_name, last=last_name)

        if has_first_name is True:
            return first_name

        if has_last_name is True:
            return last_name

        return ''

    def find(self, **filters):
        """
        finds persons with given filters.

        :keyword str first_name: first name.
        :keyword str last_name: last name
        :keyword str imdb_page: imdb page link
        :keyword str photo_name: photo file name.
        :keyword datetime from_add_date: from add date.
        :keyword datetime to_add_date: to add date.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to True if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to True if not provided.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[tuple] joins: list of all join expressions to be performed on query.
                                    defaults to no join if not provided.
                                    values must be provided as a list of tuples.
                                    for example:
                                    joins=[(ActorEntity,
                                            ActorEntity.person_id == PersonEntity.id),
                                           (DirectorEntity,
                                            DirectorEntity.person_id == PersonEntity.id)]

        :rtype: list[PersonEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions, **filters)

    def exists(self, first_name, last_name):
        """
        gets a value indicating that a person with given first and last name exists.

        :param str first_name: first name.
        :param str last_name: last name

        :rtype: bool
        """

        search_name = self._get_search_name(first_name, last_name)
        store = get_current_store()
        return store.query(PersonEntity.id).filter(
            PersonEntity.search_name.ilike(search_name)).existed()

    def get_all(self, **options):
        """
        gets all persons.

        :keyword list[CoreColumn | CoreEntity] columns: list of columns or entity types
                                                        to be used in select list.
                                                        if not provided, `PersonEntity`
                                                        will be used.

        :keyword list[tuple] joins: list of all join expressions to be performed on query.
                                    defaults to no join if not provided.
                                    values must be provided as a list of tuples.
                                    for example:
                                    joins=[(ActorEntity,
                                            ActorEntity.person_id == PersonEntity.id),
                                           (DirectorEntity,
                                            DirectorEntity.person_id == PersonEntity.id)]

        :rtype: list[PersonEntity]
        """

        return self._get_all(**options)

    def get_by_name(self, first_name, last_name):
        """
        gets a person by its first and last name.

        it returns None if person does not exist.

        :param str first_name: first name.
        :param str last_name: last name

        :rtype: PersonEntity
        """

        search_name = self._get_search_name(first_name, last_name)
        store = get_current_store()
        return store.query(PersonEntity).filter(
            PersonEntity.search_name.ilike(search_name)).one_or_none()
