# -*- coding: utf-8 -*-
"""
persons models module.
"""

from sqlalchemy import Unicode, Integer, TIMESTAMP

import pyrin.globalization.datetime.services as datetime_services

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class PersonBaseEntity(CoreEntity):
    """
    person base entity class.
    """

    _table = 'person'

    id = CoreColumn('id', Integer, index=True, primary_key=True, autoincrement=True)


class PersonEntity(PersonBaseEntity):
    """
    person entity class.
    """

    _extend_existing = True

    first_name = CoreColumn('first_name', Unicode(100), nullable=False)
    last_name = CoreColumn('last_name', Unicode(100))
    search_name = CoreColumn('search_name', Unicode(200), exposed=False, nullable=False)
    imdb_page = CoreColumn('imdb_page', Unicode(150), unique=True)
    photo_name = CoreColumn('photo_name', Unicode(250), unique=True)

    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True),
                          nullable=False, default=datetime_services.now)
