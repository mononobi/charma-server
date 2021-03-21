# -*- coding: utf-8 -*-
"""
movies collector api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.collector.services as movies_collector_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return movies_collector_services.method_name(*arg, **kwargs)
