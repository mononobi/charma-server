# -*- coding: utf-8 -*-
"""
users component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.security.users import UsersPackage
from charma.security.users.manager import UsersManager


@component(UsersPackage.COMPONENT_NAME, replace=True)
class UsersComponent(Component, UsersManager):
    """
    users component class.
    """
    pass
