# -*- coding: utf-8 -*-
"""
persons validators module.
"""

from pyrin.core.globals import _
from pyrin.validator.decorators import validator
from pyrin.validator.handlers.misc import InValidator
from pyrin.validator.handlers.string import HTTPSValidator

from imovie.persons.enumerations import PersonTypeEnum
from imovie.persons.models import PersonEntity


@validator(PersonEntity, PersonEntity.imdb_page)
class PersonIMDBPageValidator(HTTPSValidator):
    """
    person imdb page validator class.
    """

    regex = r'^https://www.imdb.com/name/nm[\d]+$'

    pattern_not_match_message = _('The provided value for [{param_name}] '
                                  'is not a valid imdb person page.')


@validator(PersonEntity, 'type')
class PersonTypeValidator(InValidator):
    """
    person type validator class.
    """

    default_nullable = True
    default_is_list = True
    default_null_items = False
    default_allow_single = True
    default_valid_values = PersonTypeEnum.values()
