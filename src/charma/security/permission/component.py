# -*- coding: utf-8 -*-
"""
permission component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.security.permission import PermissionPackage
from charma.security.permission.manager import PermissionManager


@component(PermissionPackage.COMPONENT_NAME, replace=True)
class PermissionComponent(Component, PermissionManager):
    """
    permission component class.
    """
    pass
