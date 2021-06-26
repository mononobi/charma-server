# -*- coding: utf-8 -*-
"""
languages component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.languages import LanguagesPackage
from charma.languages.manager import LanguagesManager


@component(LanguagesPackage.COMPONENT_NAME)
class LanguagesComponent(Component, LanguagesManager):
    """
    languages component class.
    """
    pass
