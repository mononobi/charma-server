# -*- coding: utf-8 -*-
"""
genres models module.
"""

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, StringColumn, BooleanColumn


class GenreBaseEntity(CoreEntity):
    """
    genre base entity class.
    """

    _table = 'genre'

    id = GUIDPKColumn(name='id')


class GenreEntity(GenreBaseEntity):
    """
    genre entity class.
    """

    _extend_existing = True

    name = StringColumn(name='name', max_length=50, unique=True, nullable=False, validated=True)
    is_main = BooleanColumn(name='is_main', nullable=False, default=False, allow_write=False)
