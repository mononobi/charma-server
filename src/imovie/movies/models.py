# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Integer, Unicode, TIMESTAMP, Float, String

from pyrin.core.context import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.model.schema import CoreColumn


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    __tablename__ = 'movie'

    id = CoreColumn(name='MovieID', type_=Integer, autoincrement=True, primary_key=True)

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

    name = CoreColumn(name='MovieName', type_=Unicode)
    release_year = CoreColumn(name='ProductYear', type_=Integer)
    archive_date = CoreColumn(name='AddDate', type_=TIMESTAMP(timezone=False))
    imdb_rate = CoreColumn(name='IMDBRate', type_=Float)
    duration = CoreColumn(name='Duration', type_=String)
