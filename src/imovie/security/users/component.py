# -*- coding: utf-8 -*-
"""
users component module.
"""

from pyrin.application.decorators import component
from pyrin.application.context import Component

from imovie.security.users import UsersPackage
from imovie.security.users.manager import UsersManager


@component(UsersPackage.COMPONENT_NAME, replace=True)
class UsersComponent(Component, UsersManager):
    """
    users component class.
    """
