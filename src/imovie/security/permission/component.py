# -*- coding: utf-8 -*-
"""
permission component module.
"""

from pyrin.application.context import Component
from pyrin.application.decorators import component

from imovie.security.permission import PermissionPackage
from imovie.security.permission.manager import PermissionManager


@component(PermissionPackage.COMPONENT_NAME, replace=True)
class PermissionComponent(Component, PermissionManager):
    """
    permission component class.
    """
