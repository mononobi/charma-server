# -*- coding: utf-8 -*-
"""
languages manager module.
"""

from pyrin.core.structs import Manager

from imovie.languages import LanguagesPackage


class LanguagesManager(Manager):
    """
    languages manager class.
    """

    package_class = LanguagesPackage
