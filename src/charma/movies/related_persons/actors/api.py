# -*- coding: utf-8 -*-
"""
movies related actors api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import charma.movies.related_persons.actors.services as related_actor_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return related_actor_services.method_name(*arg, **kwargs)
