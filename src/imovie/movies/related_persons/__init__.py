# -*- coding: utf-8 -*-
"""
movies related persons package.
"""

from pyrin.packaging.base import Package


class RelatedPersonsPackage(Package):
    """
    movies related persons package class.
    """

    NAME = __name__
    DEPENDS = ['imovie.persons']
