# -*- coding: utf-8 -*-
"""
persons manager module.
"""

from pyrin.core.structs import Manager

from imovie.persons import PersonsPackage


class PersonsManager(Manager):
    """
    persons manager class.
    """

    package_class = PersonsPackage
