# -*- coding: utf-8 -*-
"""
directors models module.
"""

from sqlalchemy import Integer, ForeignKey

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class DirectorBaseEntity(CoreEntity):
    """
    director base entity class.
    """

    _table = 'director'

    person_id = CoreColumn('person_id', Integer, ForeignKey('person.id'),
                           index=True, primary_key=True, autoincrement=False)


class DirectorEntity(DirectorBaseEntity):
    """
    director entity class.
    """

    _extend_existing = True
