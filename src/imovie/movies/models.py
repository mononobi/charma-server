# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Integer, Unicode, Float, Boolean, SmallInteger, \
    CheckConstraint, and_, UniqueConstraint, TIMESTAMP

from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.types.custom import GUID
from pyrin.database.model.mixin import CreateHistoryMixin
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, FKColumn, HiddenColumn


class MovieBaseEntity(CoreEntity):
    """
    movie base entity class.
    """

    _table = 'movie'

    id = GUIDPKColumn(name='id')


class MovieEntity(MovieBaseEntity, CreateHistoryMixin):
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

    identifier = HiddenColumn(name='identifier', type_=Unicode(150), unique=True)
    title = CoreColumn(name='title', type_=Unicode(150))
    search_title = HiddenColumn(name='search_title', type_=Unicode(150))
    original_title = CoreColumn(name='original_title', type_=Unicode(150))
    search_original_title = HiddenColumn(name='search_original_title', type_=Unicode(150))
    library_title = CoreColumn(name='library_title', type_=Unicode(150), nullable=False)
    search_library_title = HiddenColumn(name='search_library_title',
                                        type_=Unicode(150), nullable=False)
    production_year = CoreColumn(name='production_year', type_=Integer)
    imdb_rate = CoreColumn(name='imdb_rate', type_=Float, nullable=False, default=0)
    meta_score = CoreColumn(name='meta_score', type_=SmallInteger, nullable=False, default=0)
    runtime = CoreColumn(name='runtime', type_=SmallInteger, nullable=False, default=0)
    imdb_page = CoreColumn(name='imdb_page', type_=Unicode(150))
    poster_name = CoreColumn(name='poster_name', type_=Unicode(250))
    directory_name = CoreColumn(name='directory_name', type_=Unicode(250), nullable=False)
    is_watched = CoreColumn(name='is_watched', type_=Boolean, nullable=False, default=False)
    storyline = CoreColumn(name='storyline', type_=Unicode(5000))
    search_storyline = HiddenColumn(name='search_storyline', type_=Unicode(5000))
    watched_date = CoreColumn(name='watched_date', type_=TIMESTAMP(timezone=True))
    content_rate = CoreColumn(name='content_rate', type_=SmallInteger)
    resolution = CoreColumn(name='resolution', type_=SmallInteger,
                            nullable=False, default=ResolutionEnum.UNKNOWN)

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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)


class FavoriteMovieEntity(FavoriteMovieBaseEntity, CreateHistoryMixin):
    """
    favorite movie entity class.
    """

    _extend_existing = True

    MIN_FAVORITE_RATE = 0
    MAX_FAVORITE_RATE = 10

    favorite_rate = CoreColumn(name='favorite_rate', type_=Integer, nullable=False)

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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)
    person_id = FKColumn(fk='actor.person_id', name='person_id', type_=GUID, primary_key=True)


class Movie2ActorEntity(Movie2ActorBaseEntity):
    """
    movie 2 actor entity class.
    """

    _extend_existing = True

    is_star = CoreColumn(name='is_star', type_=Boolean, nullable=False, default=False)
    character = CoreColumn(name='character', type_=Unicode(150))
    search_character = HiddenColumn(name='search_character', type_=Unicode(150))


class Movie2DirectorBaseEntity(CoreEntity):
    """
    movie 2 director base entity class.
    """

    _table = 'movie_2_director'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)
    person_id = FKColumn(fk='director.person_id', name='person_id', type_=GUID, primary_key=True)


class Movie2DirectorEntity(Movie2DirectorBaseEntity):
    """
    movie 2 director entity class.
    """

    _extend_existing = True

    is_main = CoreColumn(name='is_main', type_=Boolean, nullable=False, default=False)


class MovieSuggestionCacheBaseEntity(CoreEntity):
    """
    movie suggestion cache base entity class.
    """

    _table = 'movie_suggestion_cache'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)


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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)


class WatchLaterEntity(WatchLaterBaseEntity, CreateHistoryMixin):
    """
    watch later entity class.
    """

    _extend_existing = True


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

    path = CoreColumn(name='path', type_=Unicode(250), nullable=False)
    os = CoreColumn(name='os', type_=SmallInteger, nullable=False)

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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)


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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)
    genre_id = FKColumn(fk='genre.id', name='genre_id', type_=GUID, primary_key=True)


class Movie2GenreEntity(Movie2GenreBaseEntity):
    """
    movie 2 genre entity class.
    """

    _extend_existing = True

    is_main = CoreColumn(name='is_main', type_=Boolean, nullable=False, default=False)


class Movie2LanguageBaseEntity(CoreEntity):
    """
    movie 2 language base entity class.
    """

    _table = 'movie_2_language'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID, primary_key=True)
    language_id = FKColumn(fk='language.id', name='language_id', type_=GUID, primary_key=True)


class Movie2LanguageEntity(Movie2LanguageBaseEntity):
    """
    movie 2 language entity class.
    """

    _extend_existing = True
