# -*- coding: utf-8 -*-
"""
actors api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.persons.actors.services as actors_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return persons_actors_services.method_name(*arg, **kwargs)
