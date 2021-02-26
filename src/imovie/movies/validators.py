# -*- coding: utf-8 -*-
"""
movies validators module.
"""

from pyrin.core.globals import _
from pyrin.validator.decorators import validator
from pyrin.validator.handlers.misc import MinimumValidator, RangeValidator
from pyrin.validator.handlers.number import IntegerValidator, FloatValidator
from pyrin.validator.handlers.string import StringValidator

from imovie.movies.models import MovieEntity


@validator(MovieEntity, 'title')
class MovieTitleValidator(StringValidator):
    """
    movie validator class.
    """

    default_minimum_length = 1
    default_maximum_length = MovieEntity.title.type.length
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = MovieEntity.title.nullable


@validator(MovieEntity, 'original_title')
class MovieOriginalTitleValidator(StringValidator):
    """
    movie original title validator class.
    """

    default_minimum_length = 1
    default_maximum_length = MovieEntity.original_title.type.length
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = MovieEntity.original_title.nullable


@validator(MovieEntity, 'library_title')
class MovieLibraryTitleValidator(StringValidator):
    """
    movie library title validator class.
    """

    default_minimum_length = 1
    default_maximum_length = MovieEntity.library_title.type.length
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = MovieEntity.library_title.nullable


@validator(MovieEntity, 'production_year')
class MovieProductionYearValidator(IntegerValidator, MinimumValidator):
    """
    movie production year validator class.
    """

    default_nullable = MovieEntity.production_year.nullable
    default_accepted_minimum = MovieEntity.MIN_PRODUCTION_YEAR
    default_inclusive_minimum = True


@validator(MovieEntity, 'imdb_rate')
class MovieIMDBRateValidator(FloatValidator, RangeValidator):
    """
    movie imdb rate validator class.
    """

    default_nullable = MovieEntity.imdb_rate.nullable
    default_accepted_minimum = MovieEntity.MIN_IMDB_RATE
    default_accepted_maximum = MovieEntity.MAX_IMDB_RATE
    default_inclusive_minimum = True
    default_inclusive_maximum = True


@validator(MovieEntity, 'meta_score')
class MovieMetaScoreValidator(IntegerValidator, RangeValidator):
    """
    movie meta score validator class.
    """

    default_nullable = MovieEntity.meta_score.nullable
    default_accepted_minimum = MovieEntity.MIN_META_SCORE
    default_accepted_maximum = MovieEntity.MAX_META_SCORE
    default_inclusive_minimum = True
    default_inclusive_maximum = True


@validator(MovieEntity, 'runtime')
class MovieRuntimeValidator(IntegerValidator, RangeValidator):
    """
    movie runtime validator class.
    """

    default_nullable = MovieEntity.runtime.nullable
    default_accepted_minimum = 1
    default_accepted_maximum = 2000
    default_inclusive_minimum = True
    default_inclusive_maximum = True


@validator(MovieEntity, 'title')
class MovieIMDBPageValidator(StringValidator):
    """
    movie validator class.
    """

    default_minimum_length = 1
    default_maximum_length = MovieEntity.title.type.length
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = MovieEntity.title.nullable
