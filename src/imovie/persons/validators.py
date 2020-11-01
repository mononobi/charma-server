# -*- coding: utf-8 -*-
"""
persons validators module.
"""

from pyrin.core.globals import _
from pyrin.validator.decorators import validator
from pyrin.validator.handlers.string import StringValidator, HTTPSValidator

from imovie.persons.models import PersonEntity


@validator(PersonEntity, 'fullname')
class PersonFullNameValidator(StringValidator):
    """
    person fullname validator class.
    """

    default_minimum_length = 1
    default_maximum_length = 200
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = False


@validator(PersonEntity, 'imdb_page')
class PersonIMDBPageValidator(HTTPSValidator):
    """
    person imdb page validator class.
    """

    regex = r'^https://www.imdb.com/name/nm[\d]+/$'
    default_minimum_length = 30
    default_maximum_length = 150
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = True

    pattern_not_match_message = _('The provided value for [{param_name}] '
                                  'is not a valid imdb person page.')


@validator(PersonEntity, 'photo_name')
class PersonPhotoNameValidator(StringValidator):
    """
    person photo name validator class.
    """

    default_minimum_length = 1
    default_maximum_length = 250
    default_allow_blank = False
    default_allow_whitespace = False
    default_nullable = True
