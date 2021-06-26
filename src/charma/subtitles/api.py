# -*- coding: utf-8 -*-
"""
subtitles api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.subtitles.services as subtitles_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return subtitles_services.method_name(*arg, **kwargs)
