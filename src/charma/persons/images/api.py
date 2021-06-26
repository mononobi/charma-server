# -*- coding: utf-8 -*-
"""
persons images api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.persons.images.services as person_image_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return person_image_services.method_name(*arg, **kwargs)
