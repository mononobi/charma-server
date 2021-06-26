# -*- coding: utf-8 -*-
"""
persons component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.persons import PersonsPackage
from charma.persons.manager import PersonsManager


@component(PersonsPackage.COMPONENT_NAME)
class PersonsComponent(Component, PersonsManager):
    """
    persons component class.
    """
    pass
