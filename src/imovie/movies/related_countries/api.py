# -*- coding: utf-8 -*-
"""
movies related countries api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.related_countries.services as related_country_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return related_country_services.method_name(*arg, **kwargs)
