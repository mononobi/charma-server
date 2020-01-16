# -*- coding: utf-8 -*-
"""
authorization component module.
"""

from pyrin.application.context import Component
from pyrin.application.decorators import component

from imovie.security.authorization import AuthorizationPackage
from imovie.security.authorization.manager import AuthorizationManager


@component(AuthorizationPackage.COMPONENT_NAME, replace=True)
class AuthorizationComponent(Component, AuthorizationManager):
    """
    authorization component class.
    """
