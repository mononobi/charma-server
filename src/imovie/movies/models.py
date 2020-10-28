# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Integer, Unicode, TIMESTAMP, Float, Boolean, SmallInteger, \
    CheckConstraint, and_, ForeignKey, UniqueConstraint

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

    identifier = CoreColumn('identifier', Unicode(150),
                            unique=True, nullable=True, exposed=False)

    title = CoreColumn('title', Unicode(150), nullable=True)
    original_title = CoreColumn('original_title', Unicode(150), nullable=True)
    library_title = CoreColumn('library_title', Unicode(150))
    search_title = CoreColumn('search_title', Unicode(150), exposed=False)
    production_year = CoreColumn('production_year', Integer, nullable=True)
    imdb_rate = CoreColumn('imdb_rate', Float, default=0)
    meta_score = CoreColumn('meta_score', SmallInteger, default=0)
    runtime = CoreColumn('runtime', SmallInteger, default=0)
    imdb_page = CoreColumn('imdb_page', Unicode(150), nullable=True)
    poster_name = CoreColumn('poster_name', Unicode(250), nullable=True)
    directory_name = CoreColumn('directory_name', Unicode(250))
    is_watched = CoreColumn('is_watched', Boolean, default=False)
    storyline = CoreColumn('storyline', Unicode(5000), nullable=True)
    search_storyline = CoreColumn('search_storyline', Unicode(5000),
                                  nullable=True, exposed=False)

    watched_date = CoreColumn('watched_date', TIMESTAMP(timezone=True), nullable=True)
    content_rate = CoreColumn('content_rate', SmallInteger, nullable=True)
    resolution = CoreColumn('resolution', SmallInteger, default=ResolutionEnum.UNKNOWN)
    archived_date = CoreColumn('archived_date', TIMESTAMP(timezone=True),
                               index=True, default=datetime_services.now)

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

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)


class FavoriteMovieEntity(FavoriteMovieBaseEntity):
    """
    favorite movie entity class.
    """

    _extend_existing = True

    MIN_FAVORITE_RATE = 0
    MAX_FAVORITE_RATE = 10

    favorite_rate = CoreColumn('favorite_rate', Integer)
    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True), default=datetime_services.now)

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

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)

    person_id = CoreColumn('person_id', Integer, ForeignKey('actor.person_id'),
                           index=True, primary_key=True, autoincrement=False)


class Movie2ActorEntity(Movie2ActorBaseEntity):
    """
    movie 2 actor entity class.
    """

    _extend_existing = True

    is_star = CoreColumn('is_star', Boolean, default=False)
    character = CoreColumn('character', Unicode(150), nullable=True)


class Movie2DirectorBaseEntity(CoreEntity):
    """
    movie 2 director base entity class.
    """

    _table = 'movie_2_director'

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)

    person_id = CoreColumn('person_id', Integer, ForeignKey('director.person_id'),
                           index=True, primary_key=True, autoincrement=False)


class Movie2DirectorEntity(Movie2DirectorBaseEntity):
    """
    movie 2 director entity class.
    """

    _extend_existing = True

    is_main = CoreColumn('is_main', Boolean, default=False)


class MovieSuggestionCacheBaseEntity(CoreEntity):
    """
    movie suggestion cache base entity class.
    """

    _table = 'movie_suggestion_cache'

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)


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

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)


class WatchLaterEntity(WatchLaterBaseEntity):
    """
    watch later entity class.
    """

    _extend_existing = True

    add_date = CoreColumn('add_date', TIMESTAMP(timezone=True), default=datetime_services.now)


class MovieRootPathBaseEntity(CoreEntity):
    """
    movie root path base entity class.
    """

    _table = 'movie_root_path'

    id = CoreColumn('id', Integer, index=True, primary_key=True, autoincrement=True)


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

    path = CoreColumn('path', Unicode(250))
    os = CoreColumn('os', SmallInteger)

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

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)


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

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)

    genre_id = CoreColumn('genre_id', Integer, ForeignKey('genre.id'),
                          index=True, primary_key=True, autoincrement=False)


class Movie2GenreEntity(Movie2GenreBaseEntity):
    """
    movie 2 genre entity class.
    """

    _extend_existing = True

    is_main = CoreColumn('is_main', Boolean, default=False)


class Movie2LanguageBaseEntity(CoreEntity):
    """
    movie 2 language base entity class.
    """

    _table = 'movie_2_language'

    movie_id = CoreColumn('movie_id', Integer, ForeignKey('movie.id'),
                          index=True, primary_key=True, autoincrement=False)

    language_id = CoreColumn('language_id', Integer, ForeignKey('language.id'),
                             index=True, primary_key=True, autoincrement=False)


class Movie2LanguageEntity(Movie2LanguageBaseEntity):
    """
    movie 2 language entity class.
    """

    _extend_existing = True
