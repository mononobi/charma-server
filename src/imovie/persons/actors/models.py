# -*- coding: utf-8 -*-
"""
actors models module.
"""

from pyrin.database.orm.types.custom import GUID
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.columns import FKColumn


class ActorBaseEntity(CoreEntity):
    """
    actor base entity class.
    """

    _table = 'actor'

    person_id = FKColumn(fk='person.id', name='person_id', type_=GUID, primary_key=True)


class ActorEntity(ActorBaseEntity):
    """
    actor entity class.
    """

    _extend_existing = True
