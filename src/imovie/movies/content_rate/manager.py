# -*- coding: utf-8 -*-
"""
movies content rate manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.movies.models import ContentRateEntity
from imovie.movies.content_rate import ContentRatePackage
from imovie.movies.content_rate.exceptions import ContentRateDoesNotExistError


class ContentRateManager(Manager):
    """
    movies content rate manager class.
    """

    package_class = ContentRatePackage

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str name: content rate name.

        :raises ValidationError: validation error.

        :rtype: list
        """

        validator_services.validate_for_find(ContentRateEntity, filters)
        name = filters.get('name')

        if name is not None:
            expressions.append(ContentRateEntity.name.icontains(name))

    def _get(self, id):
        """
        gets content rate with given id.

        it returns None if content rate does not exist.

        :param uuid.UUID id: content rate id.

        :rtype: ContentRateEntity
        """

        store = get_current_store()
        return store.query(ContentRateEntity).get(id)

    def _get_all(self, *expressions):
        """
        gets all content rates using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :rtype: list[ContentRateEntity]
        """

        store = get_current_store()
        return store.query(ContentRateEntity).filter(*expressions)\
            .order_by(ContentRateEntity.name).all()

    def get(self, id):
        """
        gets content rate with given id.

        it raises an error if content rate does not exist.

        :param uuid.UUID id: content rate id.

        :raises ContentRateDoesNotExistError: content rate does not exist error.

        :rtype: ContentRateEntity
        """

        entity = self._get(id)
        if entity is None:
            raise ContentRateDoesNotExistError(_('Content rate with id [{id}] does not exist.')
                                               .format(id=id))
        return entity

    def create(self, name, **options):
        """
        creates a new content rate.

        :param str name: content rate name.

        :raises ValidationError: validation error.

        :returns: created content rate id.
        :rtype: uuid.UUID
        """

        options.update(name=name)
        validator_services.validate_dict(ContentRateEntity, options)
        entity = ContentRateEntity(**options)
        entity.save()
        return entity.id

    def find(self, **filters):
        """
        finds content rates with given filters.

        :keyword str name: content rate name.

        :raises ValidationError: validation error.

        :rtype: list[ContentRateEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions)

    def exists(self, name):
        """
        gets a value indicating that a content rate with given name exists.

        :param str name: content rate name.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(ContentRateEntity.id)\
            .filter(ContentRateEntity.name.ilike(name)).existed()

    def get_all(self):
        """
        gets all content rates.

        :rtype: list[ContentRateEntity]
        """

        return self._get_all()

    def delete(self, id):
        """
        deletes a content rate with given id.

        :param uuid.UUID id: content rate id.

        :returns: count of deleted items.
        :rtype: int
        """

        store = get_current_store()
        return store.query(ContentRateEntity).filter(ContentRateEntity.id == id).delete()

    def get_by_name(self, name):
        """
        gets a content rate by name.

        it returns None if content rate does not exist.

        :param str name: content rate name.

        :rtype: ContentRateEntity
        """

        store = get_current_store()
        return store.query(ContentRateEntity)\
            .filter(ContentRateEntity.name.ilike(name)).one_or_none()
