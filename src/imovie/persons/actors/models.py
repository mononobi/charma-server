# -*- coding: utf-8 -*-
"""
actors models module.
"""

from sqlalchemy import ForeignKey

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn


class ActorBaseEntity(CoreEntity):
    """
    actor base entity class.
    """

    _table = 'actor'

    person_id = GUIDPKColumn(ForeignKey('person.id'), name='person_id')


class ActorEntity(ActorBaseEntity):
    """
    actor entity class.
    """

    _extend_existing = True
