# -*- coding: utf-8 -*-
"""
search api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.search.services as search_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return search_services.method_name(*arg, **kwargs)
