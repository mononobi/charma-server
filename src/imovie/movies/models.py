# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Unicode, TIMESTAMP, Float, SmallInteger, Time, Boolean, CheckConstraint

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.context import DTO
from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.model.schema import CoreColumn
from pyrin.database.orm.types.custom import GUID


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    __tablename__ = 'movie'

    id = CoreColumn(name='id', type_=GUID, primary_key=True, nullable=False, index=True)

    def __eq__(self, other):
        if isinstance(other, MovieBaseEntity):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return '<{module}.{class_} [{pk}]>'.format(module=self.__module__,
                                                   class_=self.__class__.__name__,
                                                   pk=str(self.id))

    def __str__(self):
        return str(self.id)


class MovieEntity(MovieBaseEntity):
    """
    movie entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    class QualityEnum(CoreEnum):
        """
        quality enum.
        """

        UNKNOWN = 0
        VCD = 1
        DVD = 2
        HD = 3
        FULL_HD = 4
        ULTRA_HD = 5

    user_id = CoreColumn(name='user_id', type_=GUID, nullable=False, index=True)
    name = CoreColumn(name='name', type_=Unicode(100), nullable=False)
    release_year = CoreColumn(name='release_year', type_=SmallInteger)
    imdb_rate = CoreColumn(name='imdb_rate', type_=Float, default=0)
    duration = CoreColumn(name='duration', type_=Time)
    poster_link = CoreColumn(name='poster_link', type_=Unicode(250))
    folder_link = CoreColumn(name='folder_link', type_=Unicode(250), nullable=False)
    imdb_link = CoreColumn(name='imdb_link', type_=Unicode(250))
    watched = CoreColumn(name='watched', type_=Boolean, nullable=False, default=False)
    story_line = CoreColumn(name='story_line', type_=Unicode(1000))
    archive_date = CoreColumn(name='archive_date', type_=TIMESTAMP(timezone=True),
                              nullable=False, default=datetime_services.now)
    quality = CoreColumn(CheckConstraint('quality in {values}'.
                                         format(values=tuple(QualityEnum.values()))),
                         name='quality', type_=SmallInteger,
                         nullable=False, default=QualityEnum.UNKNOWN)
