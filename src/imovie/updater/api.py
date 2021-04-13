# -*- coding: utf-8 -*-
"""
updater api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.updater.services as updater_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return updater_services.method_name(*arg, **kwargs)
