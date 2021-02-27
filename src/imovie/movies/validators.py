# -*- coding: utf-8 -*-
"""
movies validators module.
"""

from pyrin.core.globals import _
from pyrin.validator.decorators import validator
from pyrin.validator.handlers.string import HTTPSValidator

from imovie.movies.models import MovieEntity


@validator(MovieEntity, MovieEntity.imdb_page)
class MovieIMDBPageValidator(HTTPSValidator):
    """
    movie imdb page validator class.
    """

    regex = r'^https://www.imdb.com/title/tt[\d]+/$'

    pattern_not_match_message = _('The provided value for [{param_name}] '
                                  'is not a valid imdb movie page.')
