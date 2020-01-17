# -*- coding: utf-8 -*-
"""
movies api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.movies.services as movie_services


@api('/movies/find', methods=HTTPMethodEnum.GET, login_required=False)
def find(**filters):
    """
    """

    return movie_services.find(**filters)
