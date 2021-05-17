# -*- coding: utf-8 -*-
"""
directors stats manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.persons.directors.models import DirectorEntity
from imovie.persons.directors.stats import DirectorsStatsPackage


class DirectorsStatsManager(Manager):
    """
    directors stats manager class.
    """

    package_class = DirectorsStatsPackage

    def get_count(self):
        """
        gets total count of directors.

        :rtype: int
        """

        store = get_current_store()
        return store.query(DirectorEntity.person_id).count()

    def get_stats(self):
        """
        gets different stats of directors.

        :returns: dict(int directors_count: total directors count)
        :rtype: dict
        """

        count = self.get_count()
        return dict(directors_count=count)
