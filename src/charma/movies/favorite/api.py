# -*- coding: utf-8 -*-
"""
movies favorite api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.movies.favorite.services as favorite_movie_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return favorite_movie_services.method_name(*arg, **kwargs)
