# -*- coding: utf-8 -*-
"""
genres validators module.
"""

from pyrin.validator.decorators import validator
from pyrin.validator.handlers.string import StringValidator

from imovie.genres.models import GenreEntity


@validator(GenreEntity, 'name')
class GenreNameValidator(StringValidator):
    """
    genre name validator class.
    """

    default_minimum_length = 1
    default_maximum_length = 50
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = False
