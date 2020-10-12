# -*- coding: utf-8 -*-
"""
directors component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.persons.directors import DirectorsPackage
from imovie.persons.directors.manager import DirectorsManager


@component(DirectorsPackage.COMPONENT_NAME)
class DirectorsComponent(Component, DirectorsManager):
    """
    directors component class.
    """
    pass
