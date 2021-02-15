# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Integer, Unicode, TIMESTAMP, Float, Boolean, SmallInteger, \
    CheckConstraint, and_, UniqueConstraint

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.types.custom import GUID
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, FKColumn


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    _table = 'movie'

    id = GUIDPKColumn(name='id')


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

    identifier = CoreColumn('identifier', Unicode(150), unique=True,
                            nullable=True, allow_read=False, allow_write=False)

    title = CoreColumn('title', Unicode(150))
    original_title = CoreColumn('original_title', Unicode(150))
    library_title = CoreColumn('library_title', Unicode(150), nullable=False)
    search_title = CoreColumn('search_title', Unicode(150), allow_read=False,
                              allow_write=False, nullable=False)
    production_year = CoreColumn('production_year', Integer)
    imdb_rate = CoreColumn('imdb_rate', Float, nullable=False, default=0)
    meta_score = CoreColumn('meta_score', SmallInteger, nullable=False, default=0)
    runtime = CoreColumn('runtime', SmallInteger, nullable=False, default=0)
    imdb_page = CoreColumn('imdb_page', Unicode(150))
    poster_name = CoreColumn('poster_name', Unicode(250))
    directory_name = CoreColumn('directory_name', Unicode(250), nullable=False)
    is_watched = CoreColumn('is_watched', Boolean, nullable=False, default=False)
    storyline = CoreColumn('storyline', Unicode(5000))
    search_storyline = CoreColumn('search_storyline', Unicode(5000),
                                  allow_read=False, allow_write=False)
    watched_date = CoreColumn('watched_date', TIMESTAMP(timezone=True))
    content_rate = CoreColumn('content_rate', SmallInteger)

    resolution = CoreColumn('resolution', SmallInteger, nullable=False,
                            default=ResolutionEnum.UNKNOWN)

    archived_date = CoreColumn('archived_date', TIMESTAMP(timezone=True), index=True,
                               nullable=False, default=datetime_services.now)

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


class FavoriteMovieBaseEntity(CoreEntity):
    """
    favorite movie base entity class.
    """

    _table = 'favorite_movie'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)


class FavoriteMovieEntity(FavoriteMovieBaseEntity):
    """
    favorite movie entity class.
    """

    _extend_existing = True

    MIN_FAVORITE_RATE = 0
    MAX_FAVORITE_RATE = 10

    favorite_rate = CoreColumn('favorite_rate', Integer, nullable=False)
    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True),
                          nullable=False, default=datetime_services.now)

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


class Movie2ActorBaseEntity(CoreEntity):
    """
    movie 2 actor base entity class.
    """

    _table = 'movie_2_actor'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)
    person_id = FKColumn('actor.person_id', name='person_id', type_=GUID, primary_key=True)


class Movie2ActorEntity(Movie2ActorBaseEntity):
    """
    movie 2 actor entity class.
    """

    _extend_existing = True

    is_star = CoreColumn('is_star', Boolean, nullable=False, default=False)
    character = CoreColumn('character', Unicode(150))


class Movie2DirectorBaseEntity(CoreEntity):
    """
    movie 2 director base entity class.
    """

    _table = 'movie_2_director'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)
    person_id = FKColumn('director.person_id', name='person_id', type_=GUID, primary_key=True)


class Movie2DirectorEntity(Movie2DirectorBaseEntity):
    """
    movie 2 director entity class.
    """

    _extend_existing = True

    is_main = CoreColumn('is_main', Boolean, nullable=False, default=False)


class MovieSuggestionCacheBaseEntity(CoreEntity):
    """
    movie suggestion cache base entity class.
    """

    _table = 'movie_suggestion_cache'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)


class MovieSuggestionCacheEntity(MovieSuggestionCacheBaseEntity):
    """
    movie suggestion cache entity class.
    """

    _extend_existing = True


class WatchLaterBaseEntity(CoreEntity):
    """
    watch later base entity class.
    """

    _table = 'watch_later'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)


class WatchLaterEntity(WatchLaterBaseEntity):
    """
    watch later entity class.
    """

    _extend_existing = True

    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True),
                          nullable=False, default=datetime_services.now)


class MovieRootPathBaseEntity(CoreEntity):
    """
    movie root path base entity class.
    """

    _table = 'movie_root_path'

    id = GUIDPKColumn(name='id')


class MovieRootPathEntity(MovieRootPathBaseEntity):
    """
    movie root path entity class.
    """

    _extend_existing = True

    class OSEnum(CoreEnum):
        """
        os enum.
        """

        LINUX = 0
        WINDOWS = 1
        MAC = 2
        ANDROID = 3
        IOS = 4

    path = CoreColumn('path', Unicode(250), nullable=False)
    os = CoreColumn('os', SmallInteger, nullable=False)

    @classmethod
    def _customize_table_args(cls, table_args):
        """
        customizes different table args for current entity type.

        :param dict table_args: a dict containing different table args.
                                any changes to this dict must be done in-place.

        :rtype: tuple | object
        """

        constraints = (CheckConstraint(cls.os.in_(cls.OSEnum.values())),
                       UniqueConstraint(cls.os, cls.path))

        return constraints


class CopyRequestedMovieBaseEntity(CoreEntity):
    """
    copy requested movie base entity class.
    """

    _table = 'copy_requested_movie'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)


class CopyRequestedMovieEntity(CopyRequestedMovieBaseEntity):
    """
    copy requested movie entity class.
    """

    _extend_existing = True


class Movie2GenreBaseEntity(CoreEntity):
    """
    movie 2 genre base entity class.
    """

    _table = 'movie_2_genre'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)
    genre_id = FKColumn('genre.id', name='genre_id', type_=GUID, primary_key=True)


class Movie2GenreEntity(Movie2GenreBaseEntity):
    """
    movie 2 genre entity class.
    """

    _extend_existing = True

    is_main = CoreColumn('is_main', Boolean, nullable=False, default=False)


class Movie2LanguageBaseEntity(CoreEntity):
    """
    movie 2 language base entity class.
    """

    _table = 'movie_2_language'

    movie_id = FKColumn('movie.id', name='movie_id', type_=GUID, primary_key=True)
    language_id = FKColumn('language.id', name='language_id', type_=GUID, primary_key=True)


class Movie2LanguageEntity(Movie2LanguageBaseEntity):
    """
    movie 2 language entity class.
    """

    _extend_existing = True
