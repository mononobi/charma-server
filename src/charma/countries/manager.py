# -*- coding: utf-8 -*-
"""
countries manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from charma.countries.models import CountryEntity
from charma.countries.exceptions import CountryDoesNotExistError
from charma.countries import CountriesPackage


class CountriesManager(Manager):
    """
    countries manager class.
    """

    package_class = CountriesPackage

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str name: country name.

        :raises ValidationError: validation error.

        :rtype: list
        """

        validator_services.validate_for_find(CountryEntity, filters)
        name = filters.get('name')

        if name is not None:
            expressions.append(CountryEntity.name.icontains(name))

    def _get(self, id):
        """
        gets country with given id.

        it returns None if country does not exist.

        :param uuid.UUID id: country id.

        :rtype: CountryEntity
        """

        store = get_current_store()
        return store.query(CountryEntity).get(id)

    def _get_all(self, *expressions):
        """
        gets all countries using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :rtype: list[CountryEntity]
        """

        store = get_current_store()
        return store.query(CountryEntity).filter(*expressions)\
            .order_by(CountryEntity.name).all()

    def get(self, id):
        """
        gets country with given id.

        it raises an error if country does not exist.

        :param uuid.UUID id: country id.

        :raises CountryDoesNotExistError: country does not exist error.

        :rtype: CountryEntity
        """

        entity = self._get(id)
        if entity is None:
            raise CountryDoesNotExistError(_('Country with id [{id}] does not exist.')
                                           .format(id=id))
        return entity

    def create(self, name, **options):
        """
        creates a new country.

        :param str name: country name.

        :raises ValidationError: validation error.

        :returns: created country id.
        :rtype: uuid.UUID
        """

        options.update(name=name)
        validator_services.validate_dict(CountryEntity, options)
        entity = CountryEntity(**options)
        entity.save()
        return entity.id

    def find(self, **filters):
        """
        finds countries with given filters.

        :keyword str name: country name.

        :raises ValidationError: validation error.

        :rtype: list[CountryEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions)

    def exists(self, name):
        """
        gets a value indicating that a country with given name exists.

        :param str name: country name.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(CountryEntity.id).filter(CountryEntity.name.ilike(name)).existed()

    def get_all(self):
        """
        gets all countries.

        :rtype: list[CountryEntity]
        """

        return self._get_all()

    def delete(self, id):
        """
        deletes a country with given id.

        :param uuid.UUID id: country id.

        :returns: count of deleted items.
        :rtype: int
        """

        store = get_current_store()
        return store.query(CountryEntity).filter(CountryEntity.id == id).delete()

    def get_by_name(self, name):
        """
        gets a country by name.

        it returns None if country does not exist.

        :param str name: country name.

        :rtype: CountryEntity
        """

        store = get_current_store()
        return store.query(CountryEntity).filter(CountryEntity.name.ilike(name)).one_or_none()
