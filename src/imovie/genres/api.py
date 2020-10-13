# -*- coding: utf-8 -*-
"""
genres api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.genres.services as genres_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return genres_services.method_name(*arg, **kwargs)
