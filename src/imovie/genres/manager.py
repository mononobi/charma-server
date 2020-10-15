# -*- coding: utf-8 -*-
"""
genres manager module.
"""

import pyrin.configuration.services as config_services
import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.genres import GenresPackage
from imovie.genres.models import GenreEntity
from imovie.genres.exceptions import GenreDoesNotExistError


class GenresManager(Manager):
    """
    genres manager class.
    """

    package_class = GenresPackage

    def __init__(self):
        """
        initializes an instance of GenresManager.
        """

        super().__init__()

        self._main_genres = self._get_main_genres()

    def _get_main_genres(self):
        """
        gets list of main genres from config store.

        :rtype: list[str]
        """

        genres = config_services.get('genres', 'general', 'main_genres', default=[])
        result = []
        for item in genres:
            result.append(item.lower())

        return result

    def _is_main(self, name):
        """
        gets a value indicating that given genre is a main genre.

        :param str name: genre name.

        :rtype: bool
        """

        return name.lower() in self._main_genres

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str name: genre name.
        :keyword bool is_main: is main genre.

        :rtype: list
        """

        name = filters.get('name', None)
        is_main = filters.get('is_main', None)

        if name is not None:
            expressions.append(GenreEntity.name.icontains(name))

        if is_main is not None:
            expressions.append(GenreEntity.is_main == is_main)

    def _get(self, id):
        """
        gets genre with given id.

        it returns None if genre does not exist.

        :param int id: genre id.

        :rtype: GenreEntity
        """

        store = get_current_store()
        return store.query(GenreEntity).get(id)

    def _get_all(self, *expressions):
        """
        gets all genres using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :rtype: list[GenreEntity]
        """

        store = get_current_store()
        return store.query(GenreEntity).filter(*expressions).all()

    def get(self, id):
        """
        gets genre with given id.

        it raises an error if genre does not exist.

        :param int id: genre id.

        :raises GenreDoesNotExistError: genre does not exist error.

        :rtype: GenreEntity
        """

        entity = self._get(id)
        if entity is None:
            raise GenreDoesNotExistError(_('Genre with id [{id}] does not exist.')
                                         .format(id=id))
        return entity

    def create(self, name, **options):
        """
        creates a new genre.

        :param str name: genre name.

        :raises ValidationError: validation error.

        :returns: created genre id.
        :rtype: int
        """

        options.update(name=name)
        validator_services.validate_dict(GenreEntity, options)
        is_main = self._is_main(name)
        options.update(is_main=is_main)
        entity = GenreEntity(**options)
        entity.save()
        return entity.id

    def find(self, **filters):
        """
        finds genres with given filters.

        :keyword str name: genre name.
        :keyword bool is_main: is main genre.

        :rtype: list[GenreEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions)

    def exists(self, name):
        """
        gets a value indicating that a genre with given name exists.

        :param str name: genre name.

        :rtype: bool
        """

        store = get_current_store()
        return store.query(GenreEntity.id).filter(GenreEntity.name.ilike(name)).existed()

    def get_all(self):
        """
        gets all genres.

        :rtype: list[GenreEntity]
        """

        return self._get_all()

    def delete(self, id):
        """
        deletes a genre with given id.

        :param int id: genre id.

        :returns: count of deleted items.
        :rtype: int
        """

        store = get_current_store()
        return store.query(GenreEntity.id).filter(GenreEntity.id == id).delete()

    def get_by_name(self, name):
        """
        gets a genre by name.

        it returns None if genre does not exist.

        :param str name: genre name.

        :rtype: GenreEntity
        """

        store = get_current_store()
        return store.query(GenreEntity).filter(GenreEntity.name.ilike(name)).one_or_none()
