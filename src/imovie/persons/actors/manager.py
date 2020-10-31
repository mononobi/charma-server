# -*- coding: utf-8 -*-
"""
actors manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.persons.actors import ActorsPackage
from imovie.persons.actors.models import ActorEntity
from imovie.persons.models import PersonEntity
from imovie.persons.queries import PersonsQueries


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

    def create(self, person_id, **options):
        """
        creates a new actor.

        :param int person_id: person id.
        """

        entity = ActorEntity()
        entity.person_id = person_id
        entity.save()
