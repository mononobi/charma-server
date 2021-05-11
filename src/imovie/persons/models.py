# -*- coding: utf-8 -*-
"""
persons models module.
"""

from sqlalchemy import Unicode

from pyrin.database.model.declarative import CoreEntity
from pyrin.database.model.mixin import CreateHistoryMixin
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, HiddenColumn, StringColumn


class PersonBaseEntity(CoreEntity):
    """
    person base entity class.
    """

    _table = 'person'

    id = GUIDPKColumn(name='id')


class PersonEntity(PersonBaseEntity, CreateHistoryMixin):
    """
    person entity class.
    """

    _extend_existing = True

    fullname = StringColumn(name='fullname', max_length=200, nullable=False, validated=True)
    search_name = HiddenColumn(name='search_name', type_=Unicode(200), nullable=False, index=True)
    imdb_page = StringColumn(name='imdb_page', min_length=29, max_length=150,
                             unique=True, validated=True)
    identifier = HiddenColumn(name='identifier', type_=Unicode(150), unique=True, index=True)
    photo_name = StringColumn(name='photo_name', max_length=250, unique=True, validated=True)
