# -*- coding: utf-8 -*-
"""
languages manager module.
"""

import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.languages import LanguagesPackage
from imovie.languages.models import LanguageEntity
from imovie.languages.exceptions import LanguageDoesNotExistError


class LanguagesManager(Manager):
    """
    languages manager class.
    """

    package_class = LanguagesPackage

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str name: language name.

        :rtype: list
        """

        name = filters.get('name', None)

        if name is not None:
            expressions.append(LanguageEntity.name.icontains(name))

    def _get(self, id):
        """
        gets language with given id.

        it returns None if language does not exist.

        :param int id: language id.

        :rtype: LanguageEntity
        """

        store = get_current_store()
        return store.query(LanguageEntity).get(id)

    def _get_all(self, *expressions):
        """
        gets all languages using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :rtype: list[LanguageEntity]
        """

        store = get_current_store()
        return store.query(LanguageEntity).filter(*expressions).all()

    def get(self, id):
        """
        gets language with given id.

        it raises an error if language does not exist.

        :param int id: language id.

        :raises LanguageDoesNotExistError: language does not exist error.

        :rtype: LanguageEntity
        """

        entity = self._get(id)
        if entity is None:
            raise LanguageDoesNotExistError(_('Language with id [{id}] does not exist.')
                                            .format(id=id))
        return entity

    def create(self, name, **options):
        """
        creates a new language.

        :param str name: language name.

        :raises ValidationError: validation error.

        :returns: created language id.
        :rtype: int
        """

        options.update(name=name)
        validator_services.validate_dict(LanguageEntity, options)
        entity = LanguageEntity(**options)
        entity.save(flush=True)
        return entity.id

    def find(self, **filters):
        """
        finds languages with given filters.

        :keyword str name: language name.

        :rtype: list[LanguageEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions)

    def exists(self, name):
        """
        gets a value indicating that a language with given name exists.

        :param str name: language name.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(LanguageEntity.id).filter(LanguageEntity.name.ilike(name)).existed()

    def get_all(self):
        """
        gets all languages.

        :rtype: list[LanguageEntity]
        """

        return self._get_all()

    def delete(self, id):
        """
        deletes a language with given id.

        :param int id: language id.

        :returns: count of deleted items.
        :rtype: int
        """

        store = get_current_store()
        return store.query(LanguageEntity.id).filter(LanguageEntity.id == id).delete()

    def get_by_name(self, name):
        """
        gets a language by name.

        it returns None if language does not exist.

        :param str name: language name.

        :rtype: LanguageEntity
        """

        store = get_current_store()
        return store.query(LanguageEntity).filter(LanguageEntity.name.ilike(name)).one_or_none()
