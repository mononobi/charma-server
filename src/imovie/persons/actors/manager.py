# -*- coding: utf-8 -*-
"""
actors manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.persons.actors import ActorsPackage
from imovie.persons.actors.models import ActorEntity


class ActorsManager(Manager):
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
        return store.query(ActorEntity).get(id)
