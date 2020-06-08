# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy.dialects.sqlite import TIME
from sqlalchemy import Integer, Unicode, TIMESTAMP, Float, Boolean, SmallInteger, CheckConstraint

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.structs import DTO
from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.types.custom import GUID


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    __tablename__ = 'movie'

    id = CoreColumn('id', GUID, index=True, primary_key=True)


class MovieEntity(MovieBaseEntity):
    """
    movie entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    class ResolutionEnum(CoreEnum):
        """
        resolution enum.
        """

        UNKNOWN = 0
        VCD = 1
        DVD = 2
        HD = 3
        FHD = 4
        UHD = 5

    class ContentRateEnum(CoreEnum):
        """
        content rate enum.
        """

        UNKNOWN = 0
        G = 1
        PG = 2
        PG_13 = 3
        R = 4
        NC_17 = 5

    title = CoreColumn('title', Unicode(150), nullable=False)
    original_title = CoreColumn('original_title', Unicode(150))
    production_year = CoreColumn('production_year', Integer,
                                 CheckConstraint('production_year > 1900'))
    imdb_rate = CoreColumn('imdb_rate', Float, default=0)
    meta_score = CoreColumn('meta_score', SmallInteger, default=0)
    duration = CoreColumn('duration', TIME(truncate_microseconds=True))
    imdb_page = CoreColumn('imdb_page', Unicode(150))
    poster_name = CoreColumn('poster_name', Unicode(250))
    directory_name = CoreColumn('directory_name', Unicode(250), nullable=False)
    is_watched = CoreColumn('is_watched', Boolean, nullable=False, default=False)
    storyline = CoreColumn('storyline', Unicode(5000))
    poster_url = CoreColumn('poster_url', Unicode(600))
    watched_date = CoreColumn('watched_date', TIMESTAMP(timezone=True))
    content_rate = CoreColumn('content_rate', SmallInteger, nullable=False,
                              default=ContentRateEnum.UNKNOWN)
    resolution = CoreColumn('resolution', SmallInteger, nullable=False,
                            default=ResolutionEnum.UNKNOWN)
    archive_date = CoreColumn('archive_date', TIMESTAMP(timezone=True),
                              nullable=False, default=datetime_services.now)
