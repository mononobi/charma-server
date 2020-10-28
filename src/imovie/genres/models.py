# -*- coding: utf-8 -*-
"""
genres models module.
"""

from sqlalchemy import Integer, Unicode, Boolean

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class GenreBaseEntity(CoreEntity):
    """
    genre base entity class.
    """

    _table = 'genre'

    id = CoreColumn('id', Integer, index=True, primary_key=True, autoincrement=True)


class GenreEntity(GenreBaseEntity):
    """
    genre entity class.
    """

    _extend_existing = True

    name = CoreColumn('name', Unicode(50), unique=True, nullable=False)
    is_main = CoreColumn('is_main', Boolean, nullable=False, default=False)
