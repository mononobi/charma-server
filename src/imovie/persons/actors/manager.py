# -*- coding: utf-8 -*-
"""
actors manager module.
"""

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.persons.actors import ActorsPackage
from imovie.persons.actors.models import ActorEntity
from imovie.persons.models import PersonEntity
from imovie.persons.queries import PersonsQueries
from imovie.persons.actors.exceptions import ActorDoesNotExistError


class ActorsManager(Manager, PersonsQueries):
    """
    actors manager class.
    """

    package_class = ActorsPackage

    def _get(self, id):
        """
        gets actor with given id.

        it returns None if actor does not exist.

        :param int id: person id.

        :rtype: ActorEntity
        """

        store = get_current_store()
        return store.query(PersonEntity)\
            .filter(self._actor_exists(id), PersonEntity.id == id).one_or_none()

    def _actor_exists(self, id):
        """
        gets the required expression to check that given id is related to an actor.

        the result of this method must be used inside a where clause of another query.

        :param int id: person id.

        :returns: exists expression.
        """

        store = get_current_store()
        return store.query(ActorEntity.person_id)\
            .filter(ActorEntity.person_id == id).exists()

    def _prepare_query(self, query):
        """
        prepares given query object to limit result to actors only.

        :param CoreQuery query: query object to be prepared.

        :rtype: CoreQuery
        """

        return query.join(ActorEntity, ActorEntity.person_id == PersonEntity.id)

    def get(self, id):
        """
        gets actor with given id.

        it raises an error if actor does not exist.

        :param int id: person id.

        :raises ActorDoesNotExistError: actor does not exist error.

        :rtype: PersonEntity
        """

        entity = self._get(id)
        if entity is None:
            raise ActorDoesNotExistError(_('Actor with id [{id}] does not exist.')
                                         .format(id=id))
        return entity

    def create(self, id, **options):
        """
        creates a new actor.

        :param int id: person id.
        """

        entity = ActorEntity()
        entity.person_id = id
        entity.save()

    def delete(self, id):
        """
        deletes an actor with given id.

        :param int id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        store = get_current_store()
        return store.query(ActorEntity.person_id)\
            .filter(ActorEntity.person_id == id).delete()
