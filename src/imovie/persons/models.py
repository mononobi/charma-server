# -*- coding: utf-8 -*-
"""
persons models module.
"""

from sqlalchemy import Unicode, TIMESTAMP

import pyrin.globalization.datetime.services as datetime_services

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, HiddenColumn


class PersonBaseEntity(CoreEntity):
    """
    person base entity class.
    """

    _table = 'person'

    id = GUIDPKColumn(name='id')


class PersonEntity(PersonBaseEntity):
    """
    person entity class.
    """

    _extend_existing = True

    fullname = CoreColumn(name='fullname', type_=Unicode(200), nullable=False)
    search_name = HiddenColumn(name='search_name', type_=Unicode(200), nullable=False, index=True)
    imdb_page = CoreColumn(name='imdb_page', type_=Unicode(150), unique=True)
    identifier = HiddenColumn(name='identifier', type_=Unicode(150), unique=True, index=True)
    photo_name = CoreColumn(name='photo_name', type_=Unicode(250), unique=True)

    add_date = CoreColumn(name='add_date', type_=TIMESTAMP(timezone=True),
                          nullable=False, default=datetime_services.now, allow_write=False)
