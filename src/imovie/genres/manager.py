# -*- coding: utf-8 -*-
"""
genres manager module.
"""

from pyrin.core.structs import Manager

from imovie.genres import GenresPackage


class GenresManager(Manager):
    """
    genres manager class.
    """

    package_class = GenresPackage
