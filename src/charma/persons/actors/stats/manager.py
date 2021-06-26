# -*- coding: utf-8 -*-
"""
actors stats manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from charma.persons.actors.models import ActorEntity
from charma.persons.actors.stats import ActorsStatsPackage


class ActorsStatsManager(Manager):
    """
    actors stats manager class.
    """

    package_class = ActorsStatsPackage

    def get_count(self):
        """
        gets total count of actors.

        :rtype: int
        """

        store = get_current_store()
        return store.query(ActorEntity.person_id).count()

    def get_stats(self):
        """
        gets different stats of actors.

        :returns: dict(int actors_count: total actors count)
        :rtype: dict
        """

        count = self.get_count()
        return dict(actors_count=count)
