# -*- coding: utf-8 -*-
"""
actors component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.persons.actors import ActorsPackage
from imovie.persons.actors.manager import ActorsManager


@component(ActorsPackage.COMPONENT_NAME)
class ActorsComponent(Component, ActorsManager):
    """
    actors component class.
    """
    pass
