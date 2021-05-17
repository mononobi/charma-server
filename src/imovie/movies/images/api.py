# -*- coding: utf-8 -*-
"""
movies images api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.images.services as movies_images_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return movies_images_services.method_name(*arg, **kwargs)
