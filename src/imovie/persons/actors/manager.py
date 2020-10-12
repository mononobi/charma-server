# -*- coding: utf-8 -*-
"""
actors manager module.
"""

from pyrin.core.structs import Manager

from imovie.persons.actors import ActorsPackage


class ActorsManager(Manager):
    """
    actors manager class.
    """

    package_class = ActorsPackage
