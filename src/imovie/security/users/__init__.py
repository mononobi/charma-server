# -*- coding: utf-8 -*-
"""
users package.
"""

from pyrin.packaging.context import Package


class UsersPackage(Package):
    """
    users package class.
    """

    NAME = __name__
    DEPENDS = []
    COMPONENT_NAME = 'security.users.component'
