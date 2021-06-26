# -*- coding: utf-8 -*-
"""
countries models module.
"""

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, StringColumn


class CountryBaseEntity(CoreEntity):
    """
    country base entity class.
    """

    _table = 'country'

    id = GUIDPKColumn(name='id')


class CountryEntity(CountryBaseEntity):
    """
    country entity class.
    """

    _extend_existing = True

    name = StringColumn(name='name', max_length=50, nullable=False, unique=True, validated=True)
