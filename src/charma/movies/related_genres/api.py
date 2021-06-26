# -*- coding: utf-8 -*-
"""
movies related genres api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.movies.related_genres.services as related_genre_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return related_genre_services.method_name(*arg, **kwargs)
