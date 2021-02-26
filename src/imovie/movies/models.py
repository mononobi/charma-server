# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Integer, Unicode, Float, Boolean, SmallInteger, \
    UniqueConstraint, TIMESTAMP

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.types.custom import GUID
from pyrin.database.model.mixin import CreateHistoryMixin
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, FKColumn, HiddenColumn, \
    StringColumn


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
    title = StringColumn(name='title', max_length=150, validated=True)
    search_title = HiddenColumn(name='search_title', type_=Unicode(150))
    original_title = StringColumn(name='original_title', max_length=150, validated=True)
    search_original_title = HiddenColumn(name='search_original_title', type_=Unicode(150))
    library_title = StringColumn(name='library_title', max_length=150,
                                 nullable=False, validated=True)
    search_library_title = HiddenColumn(name='search_library_title',
                                        type_=Unicode(150), nullable=False)
    production_year = CoreColumn(name='production_year', type_=Integer, min_value=1900,
                                 max_value=datetime_services.current_year, validated=True)
    imdb_rate = CoreColumn(name='imdb_rate', type_=Float, nullable=False, default=0,
                           min_value=0, max_value=10, validated=True)
    meta_score = CoreColumn(name='meta_score', type_=SmallInteger, nullable=False,
                            default=0, min_value=0, max_value=100, validated=True)
    runtime = CoreColumn(name='runtime', type_=SmallInteger, nullable=False,
                         default=0, min_value=0, max_value=1200, validated=True)
    imdb_page = StringColumn(name='imdb_page', max_length=150, validated=True)
    poster_name = StringColumn(name='poster_name', max_length=250, validated=True)
    directory_name = StringColumn(name='directory_name', max_length=250,
                                  nullable=False, validated=True)
    is_watched = CoreColumn(name='is_watched', type_=Boolean, nullable=False,
                            default=False, validated=True)
    storyline = StringColumn(name='storyline', max_length=5000, validated=True)
    search_storyline = HiddenColumn(name='search_storyline', type_=Unicode(5000))
    watched_date = CoreColumn(name='watched_date', type_=TIMESTAMP(timezone=True), validated=True)
    content_rate = CoreColumn(name='content_rate', type_=SmallInteger,
                              validated=True, default=ContentRateEnum.UNKNOWN,
                              nullable=False, check_in=ContentRateEnum.values())
    resolution = CoreColumn(name='resolution', type_=SmallInteger,
                            nullable=False, default=ResolutionEnum.UNKNOWN,
                            check_in=ResolutionEnum.values(), validated=True)


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

    favorite_rate = CoreColumn(name='favorite_rate', type_=Integer, nullable=False,
                               min_value=0, max_value=10, validated=True)


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

    is_star = CoreColumn(name='is_star', type_=Boolean, nullable=False,
                         default=False, validated=True)
    character = StringColumn(name='character', max_length=150, validated=True)
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

    is_main = CoreColumn(name='is_main', type_=Boolean, nullable=False,
                         default=False, validated=True)


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

    path = StringColumn(name='path', max_length=250, nullable=False, validated=True)
    os = CoreColumn(name='os', type_=SmallInteger, nullable=False,
                    validated=True, check_in=OSEnum.values())

    _unique_on = os, path


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

    is_main = CoreColumn(name='is_main', type_=Boolean, nullable=False,
                         default=False, validated=True)


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
