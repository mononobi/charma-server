# -*- coding: utf-8 -*-
"""
directors manager module.
"""

from pyrin.core.globals import _
from pyrin.core.mixin import HookMixin
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.persons.directors import DirectorsPackage
from imovie.persons.directors.hooks import DirectorHookBase
from imovie.persons.directors.models import DirectorEntity
from imovie.persons.models import PersonEntity
from imovie.persons.queries import PersonsQueries
from imovie.persons.directors.exceptions import DirectorDoesNotExistError, \
    InvalidDirectorHookTypeError


class DirectorsManager(Manager, PersonsQueries, HookMixin):
    """
    directors manager class.
    """

    package_class = DirectorsPackage
    hook_type = DirectorHookBase
    invalid_hook_type_error = InvalidDirectorHookTypeError

    def _get(self, id):
        """
        gets director with given id.

        it returns None if director does not exist.

        :param uuid.UUID id: person id.

        :rtype: DirectorEntity
        """

        store = get_current_store()
        return store.query(PersonEntity)\
            .filter(self._director_exists(id), PersonEntity.id == id).one_or_none()

    def _director_exists(self, id):
        """
        gets the required expression to check that given id is related to a director.

        the result of this method must be used inside a where clause of another query.

        :param uuid.UUID id: person id.

        :returns: exists expression.
        """

        store = get_current_store()
        return store.query(DirectorEntity.person_id)\
            .filter(DirectorEntity.person_id == id).exists()

    def _prepare_query(self, query):
        """
        prepares given query object to limit result to directors only.

        :param CoreQuery query: query object to be prepared.

        :rtype: CoreQuery
        """

        return query.join(DirectorEntity, DirectorEntity.person_id == PersonEntity.id)

    def get(self, id):
        """
        gets director with given id.

        it raises an error if director does not exist.

        :param uuid.UUID id: person id.

        :raises DirectorDoesNotExistError: director does not exist error.

        :rtype: PersonEntity
        """

        entity = self._get(id)
        if entity is None:
            raise DirectorDoesNotExistError(_('Director with id [{id}] does not exist.')
                                            .format(id=id))
        return entity

    def create(self, id, **options):
        """
        creates a new director.

        :param uuid.UUID id: person id.
        """

        entity = DirectorEntity()
        entity.person_id = id
        entity.save()

    def delete(self, id):
        """
        deletes a director with given id.

        :param uuid.UUID id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        for hook in self._get_hooks():
            hook.before_delete(id)

        store = get_current_store()
        return store.query(DirectorEntity.person_id)\
            .filter(DirectorEntity.person_id == id).delete()
