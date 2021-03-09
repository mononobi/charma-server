# -*- coding: utf-8 -*-
"""
movies related directors manager module.
"""

from pyrin.core.structs import Manager

from imovie.movies.related_persons.directors import RelatedDirectorsPackage


class RelatedDirectorsManager(Manager):
    """
    movies related directors manager class.
    """

    package_class = RelatedDirectorsPackage
