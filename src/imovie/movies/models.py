# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy.dialects.sqlite import TIME
from sqlalchemy import Integer, Unicode, TIMESTAMP, Float, Boolean, SmallInteger, \
    CheckConstraint, and_, ForeignKey

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    _table = 'movie'

    id = CoreColumn('id', Integer, index=True, primary_key=True, autoincrement=True)


class MovieEntity(MovieBaseEntity):
    """
    movie entity class.
    """

    _extend_existing = True

    MIN_PRODUCTION_YEAR = 1900

    MIN_IMDB_RATE = 0
    MAX_IMDB_RATE = 10

    MIN_META_SCORE = 0
    MAX_META_SCORE = 100

    @classmethod
    def _customize_table_args(cls, table_args):
        """
        customizes different table args for current entity type.

        :param dict table_args: a dict containing different table args.
                                any changes to this dict must be done in-place.

        :rtype: tuple | object
        """

        constraints = (CheckConstraint(cls.production_year >= cls.MIN_PRODUCTION_YEAR),
                       CheckConstraint(and_(cls.imdb_rate <= cls.MAX_IMDB_RATE,
                                            cls.imdb_rate >= cls.MIN_IMDB_RATE)),
                       CheckConstraint(and_(cls.meta_score <= cls.MAX_META_SCORE,
                                            cls.meta_score >= cls.MIN_META_SCORE)),
                       CheckConstraint(cls.content_rate.in_(cls.ContentRateEnum.values())),
                       CheckConstraint(cls.resolution.in_(cls.ResolutionEnum.values())))

        return constraints

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

    title = CoreColumn('title', Unicode(150))
    original_title = CoreColumn('original_title', Unicode(150), nullable=True)
    library_title = CoreColumn('library_title', Unicode(150))
    search_title = CoreColumn('search_title', Unicode(150))
    production_year = CoreColumn('production_year', Integer, nullable=True)
    imdb_rate = CoreColumn('imdb_rate', Float, default=0)
    meta_score = CoreColumn('meta_score', SmallInteger, default=0)
    duration = CoreColumn('duration', TIME(truncate_microseconds=True), nullable=True)
    imdb_page = CoreColumn('imdb_page', Unicode(150), nullable=True)
    poster_name = CoreColumn('poster_name', Unicode(250), nullable=True)
    directory_name = CoreColumn('directory_name', Unicode(250))
    is_watched = CoreColumn('is_watched', Boolean, default=False)
    storyline = CoreColumn('storyline', Unicode(5000), nullable=True)
    poster_url = CoreColumn('poster_url', Unicode(600), nullable=True)
    watched_date = CoreColumn('watched_date', TIMESTAMP(timezone=True), nullable=True)
    content_rate = CoreColumn('content_rate', SmallInteger, nullable=True)
    resolution = CoreColumn('resolution', SmallInteger, default=ResolutionEnum.UNKNOWN)
    archive_date = CoreColumn('archive_date', TIMESTAMP(timezone=True),
                              index=True, default=datetime_services.now)


class FavoriteMovieBaseEntity(CoreEntity):
    """
    favorite movie base entity class.
    """

    _table = 'favorite_movie'

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)


class FavoriteMovieEntity(FavoriteMovieBaseEntity):
    """
    favorite movie entity class.
    """

    _extend_existing = True

    MIN_FAVORITE_RATE = 0
    MAX_FAVORITE_RATE = 10

    @classmethod
    def _customize_table_args(cls, table_args):
        """
        customizes different table args for current entity type.

        :param dict table_args: a dict containing different table args.
                                any changes to this dict must be done in-place.

        :rtype: tuple | object
        """

        return CheckConstraint(and_(cls.favorite_rate <= cls.MAX_FAVORITE_RATE,
                                    cls.favorite_rate >= cls.MIN_FAVORITE_RATE))

    favorite_rate = CoreColumn('favorite_rate', Integer)
    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True), default=datetime_services.now)
