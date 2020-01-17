# -*- coding: utf-8 -*-
"""
movies services module.
"""

from pyrin.application.services import get_component

from imovie.movies import MoviesPackage


def find(**filters):
    """
    """

    return get_component(MoviesPackage.COMPONENT_NAME).find(**filters)
