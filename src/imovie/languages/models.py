# -*- coding: utf-8 -*-
"""
languages models module.
"""

from sqlalchemy import Integer, Unicode

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class LanguageBaseEntity(CoreEntity):
    """
    language base entity class.
    """

    _table = 'language'

    id = CoreColumn('id', Integer, index=True, primary_key=True, autoincrement=True)


class LanguageEntity(LanguageBaseEntity):
    """
    language entity class.
    """

    _extend_existing = True

    name = CoreColumn('name', Unicode(50), nullable=False, unique=True)
