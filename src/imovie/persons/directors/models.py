# -*- coding: utf-8 -*-
"""
directors models module.
"""

from pyrin.database.orm.types.custom import GUID
from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import FKColumn


class DirectorBaseEntity(CoreEntity):
    """
    director base entity class.
    """

    _table = 'director'

    person_id = FKColumn(fk='person.id', name='person_id', type_=GUID, primary_key=True)


class DirectorEntity(DirectorBaseEntity):
    """
    director entity class.
    """

    _extend_existing = True
