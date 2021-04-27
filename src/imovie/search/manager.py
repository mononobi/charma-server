# -*- coding: utf-8 -*-
"""
search manager module.
"""

from pyrin.core.structs import Manager

from imovie.search import SearchPackage


class SearchManager(Manager):
    """
    search manager class.
    """

    package_class = SearchPackage
