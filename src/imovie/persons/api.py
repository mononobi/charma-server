# -*- coding: utf-8 -*-
"""
persons api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.persons.services as persons_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return persons_services.method_name(*arg, **kwargs)
