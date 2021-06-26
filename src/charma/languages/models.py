# -*- coding: utf-8 -*-
"""
languages models module.
"""

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, StringColumn


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

    name = StringColumn(name='name', max_length=50, nullable=False, unique=True, validated=True)
