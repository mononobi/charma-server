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
