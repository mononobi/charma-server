# -*- coding: utf-8 -*-
"""
persons package.
"""

from pyrin.packaging.base import Package


class PersonsPackage(Package):
    """
    persons package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'persons.component'
    CONFIG_STORE_NAMES = ['persons']
