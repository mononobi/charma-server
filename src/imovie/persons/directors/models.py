# -*- coding: utf-8 -*-
"""
directors models module.
"""

from sqlalchemy import ForeignKey

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn


class DirectorBaseEntity(CoreEntity):
    """
    director base entity class.
    """

    _table = 'director'

    person_id = GUIDPKColumn(ForeignKey('person.id'), name='person_id')


class DirectorEntity(DirectorBaseEntity):
    """
    director entity class.
    """

    _extend_existing = True
