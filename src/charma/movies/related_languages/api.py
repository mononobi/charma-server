# -*- coding: utf-8 -*-
"""
movies related languages api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.movies.related_languages.services as related_language_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return related_language_services.method_name(*arg, **kwargs)
