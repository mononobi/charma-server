# -*- coding: utf-8 -*-
"""
languages api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.languages.services as languages_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return languages_services.method_name(*arg, **kwargs)
