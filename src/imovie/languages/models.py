# -*- coding: utf-8 -*-
"""
languages models module.
"""

from sqlalchemy import Unicode

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn


class LanguageBaseEntity(CoreEntity):
    """
    language base entity class.
    """

    _table = 'language'

    id = GUIDPKColumn(name='id')


class LanguageEntity(LanguageBaseEntity):
    """
    language entity class.
    """

    _extend_existing = True

    name = CoreColumn(name='name', type_=Unicode(50), nullable=False, unique=True)
