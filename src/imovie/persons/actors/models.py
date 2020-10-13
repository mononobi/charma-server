# -*- coding: utf-8 -*-
"""
actors models module.
"""

from sqlalchemy import Integer, ForeignKey

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class ActorBaseEntity(CoreEntity):
    """
    actor base entity class.
    """

    _table = 'actor'

    person_id = CoreColumn('person_id', Integer, ForeignKey('person.id'),
                           index=True, primary_key=True, autoincrement=False)


class ActorEntity(ActorBaseEntity):
    """
    actor entity class.
    """

    _extend_existing = True
