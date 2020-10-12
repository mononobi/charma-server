# -*- coding: utf-8 -*-
"""
directors manager module.
"""

from pyrin.core.structs import Manager

from imovie.persons.directors import DirectorsPackage


class DirectorsManager(Manager):
    """
    directors manager class.
    """

    package_class = DirectorsPackage
