# -*- coding: utf-8 -*-
"""
persons models module.
"""

from sqlalchemy import Unicode, Integer, ForeignKey, CheckConstraint, TIMESTAMP

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

    # class ResolutionEnum(CoreEnum):
    #     """
    #     resolution enum.
    #     """
    #
    #     UNKNOWN = 0
    #     VCD = 1
    #     DVD = 2
    #     HD = 3
    #     FHD = 4
    #     UHD = 5
    #
    # class ContentRateEnum(CoreEnum):
    #     """
    #     content rate enum.
    #     """
    #
    #     UNKNOWN = 0
    #     G = 1
    #     PG = 2
    #     PG_13 = 3
    #     R = 4
    #     NC_17 = 5

    first_name = CoreColumn('first_name', Unicode(100))
    last_name = CoreColumn('last_name', Unicode(100), nullable=True)
    search_name = CoreColumn('search_name', Unicode(200))
    imdb_page = CoreColumn('imdb_page', Unicode(150), nullable=True)
    poster_url = CoreColumn('poster_url', Unicode(600), nullable=True)
    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True), default=datetime_services.now)
