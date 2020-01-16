# -*- coding: utf-8 -*-
"""
authentication component module.
"""

from pyrin.application.context import Component
from pyrin.application.decorators import component

from imovie.security.authentication import AuthenticationPackage
from imovie.security.authentication.manager import AuthenticationManager


@component(AuthenticationPackage.COMPONENT_NAME, replace=True)
class AuthenticationComponent(Component, AuthenticationManager):
    """
    authentication component class.
    """
