# -*- coding: utf-8 -*-
"""
movies models module.
"""

from sqlalchemy import Unicode, UnicodeText

from pyrin.core.enumerations import CoreEnum, EnumMember
from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.types.custom import GUID
from pyrin.database.model.mixin import CreateHistoryMixin
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, FKColumn, \
    HiddenColumn, StringColumn, IntegerColumn, FloatColumn, SmallIntegerColumn, \
    BooleanColumn, TimeStampColumn, TextColumn

import imovie.movies.services as movie_services


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

        UNKNOWN = EnumMember(0, 'NA')
        VCD = EnumMember(1, 'VCD')
        DVD = EnumMember(2, 'DVD')
        HD = EnumMember(3, '720p')
        FHD = EnumMember(4, '1080p')
        QHD = EnumMember(5, '1440p')
        UHD = EnumMember(6, '2160p')

    content_rate_id = FKColumn(fk='content_rate.id', name='content_rate_id',
                               type_=GUID, validated=True)
    identifier = HiddenColumn(name='identifier', type_=Unicode(150), unique=True)
    title = StringColumn(name='title', max_length=150, validated=True)
    search_title = HiddenColumn(name='search_title', type_=Unicode(150))
    original_title = StringColumn(name='original_title', max_length=150, validated=True)
    search_original_title = HiddenColumn(name='search_original_title', type_=Unicode(150))
    library_title = StringColumn(name='library_title', max_length=150,
                                 nullable=False, validated=True)
    search_library_title = HiddenColumn(name='search_library_title',
                                        type_=Unicode(150), nullable=False)
    production_year = IntegerColumn(name='production_year', validated=True, min_value=1900,
                                    max_value=movie_services.get_max_production_year)
    imdb_rate = FloatColumn(name='imdb_rate', min_value=0, max_value=10, validated=True)
    meta_score = SmallIntegerColumn(name='meta_score', min_value=0, max_value=100, validated=True)
    runtime = SmallIntegerColumn(name='runtime', min_value=0, max_value=1200, validated=True)
    imdb_page = StringColumn(name='imdb_page', min_length=31, max_length=150, validated=True)
    poster_name = StringColumn(name='poster_name', max_length=250, validated=True)
    directory_name = StringColumn(name='directory_name', max_length=250,
                                  nullable=False, validated=True)
    is_watched = BooleanColumn(name='is_watched', nullable=False, default=False, validated=True)
    storyline = TextColumn(name='storyline', validated=True)
    search_storyline = HiddenColumn(name='search_storyline', type_=UnicodeText)
    watched_date = TimeStampColumn(name='watched_date', validated=True,
                                   validated_find=False, validated_range=True)
    resolution = SmallIntegerColumn(name='resolution', nullable=False, validated=True,
                                    default=ResolutionEnum.UNKNOWN,
                                    check_in=ResolutionEnum.values())


class ContentRateBaseEntity(CoreEntity):
    """
    content rate base entity class.
    """

    _table = 'content_rate'

    id = GUIDPKColumn(name='id')


class ContentRateEntity(ContentRateBaseEntity):
    """
    content rate entity class.
    """

    _extend_existing = True

    name = StringColumn(name='name', max_length=20, nullable=False, unique=True, validated=True)


class FavoriteMovieBaseEntity(CoreEntity):
    """
    favorite movie base entity class.
    """

    _table = 'favorite_movie'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)


class FavoriteMovieEntity(FavoriteMovieBaseEntity, CreateHistoryMixin):
    """
    favorite movie entity class.
    """

    _extend_existing = True

    favorite_rate = IntegerColumn(name='favorite_rate', nullable=False,
                                  min_value=0, max_value=10, validated=True)


class Movie2ActorBaseEntity(CoreEntity):
    """
    movie 2 actor base entity class.
    """

    _table = 'movie_2_actor'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)

    person_id = FKColumn(fk='actor.person_id', name='person_id',
                         type_=GUID, primary_key=True, validated=True)


class Movie2ActorEntity(Movie2ActorBaseEntity):
    """
    movie 2 actor entity class.
    """

    _extend_existing = True

    is_star = BooleanColumn(name='is_star', nullable=False, default=False, validated=True)
    character = StringColumn(name='character', max_length=150, validated=True)
    search_character = HiddenColumn(name='search_character', type_=Unicode(150))


class Movie2DirectorBaseEntity(CoreEntity):
    """
    movie 2 director base entity class.
    """

    _table = 'movie_2_director'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)
    person_id = FKColumn(fk='director.person_id', name='person_id', type_=GUID,
                         primary_key=True, validated=True)


class Movie2DirectorEntity(Movie2DirectorBaseEntity):
    """
    movie 2 director entity class.
    """

    _extend_existing = True

    is_main = BooleanColumn(name='is_main', nullable=False, default=False, validated=True)


class MovieSuggestionCacheBaseEntity(CoreEntity):
    """
    movie suggestion cache base entity class.
    """

    _table = 'movie_suggestion_cache'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)


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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)


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
    os = SmallIntegerColumn(name='os', nullable=False, validated=True, check_in=OSEnum.values())

    _unique_on = os, path


class CopyRequestedMovieBaseEntity(CoreEntity):
    """
    copy requested movie base entity class.
    """

    _table = 'copy_requested_movie'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)


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

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)
    genre_id = FKColumn(fk='genre.id', name='genre_id', type_=GUID,
                        primary_key=True, validated=True)


class Movie2GenreEntity(Movie2GenreBaseEntity):
    """
    movie 2 genre entity class.
    """

    _extend_existing = True

    is_main = BooleanColumn(name='is_main', nullable=False, default=False, validated=True)


class Movie2LanguageBaseEntity(CoreEntity):
    """
    movie 2 language base entity class.
    """

    _table = 'movie_2_language'

    movie_id = FKColumn(fk='movie.id', name='movie_id', type_=GUID,
                        primary_key=True, validated=True)
    language_id = FKColumn(fk='language.id', name='language_id', type_=GUID,
                           primary_key=True, validated=True)


class Movie2LanguageEntity(Movie2LanguageBaseEntity):
    """
    movie 2 language entity class.
    """

    _extend_existing = True

    is_main = BooleanColumn(name='is_main', nullable=False, default=False, validated=True)
