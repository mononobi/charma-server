# -*- coding: utf-8 -*-
"""
genres models module.
"""

from sqlalchemy import Boolean

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, StringColumn


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
    is_main = CoreColumn(name='is_main', type_=Boolean, nullable=False,
                         default=False, allow_write=False)
