# -*- coding: utf-8 -*-
"""
movies related directors package.
"""

from pyrin.packaging.base import Package


class RelatedDirectorsPackage(Package):
    """
    movies related directors package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'movies.related_persons.directors.component'
    DEPENDS = ['imovie.persons.directors']
