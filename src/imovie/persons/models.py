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

    identifier = CoreColumn('identifier', Unicode(150), unique=True, exposed=False)
    first_name = CoreColumn('first_name', Unicode(100))
    last_name = CoreColumn('last_name', Unicode(100), nullable=True)
    search_name = CoreColumn('search_name', Unicode(200), exposed=False)
    imdb_page = CoreColumn('imdb_page', Unicode(150), nullable=True, unique=True)
    photo_name = CoreColumn('photo_name', Unicode(250), nullable=True, unique=True)
    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True), default=datetime_services.now)
