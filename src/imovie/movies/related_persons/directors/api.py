# -*- coding: utf-8 -*-
"""
movies related directors api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.related_persons.directors.services as related_director_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return related_director_services.method_name(*arg, **kwargs)
