# -*- coding: utf-8 -*-
"""
persons images component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.persons.images import PersonsImagesPackage
from charma.persons.images.manager import PersonsImagesManager


@component(PersonsImagesPackage.COMPONENT_NAME)
class PersonsImagesComponent(Component, PersonsImagesManager):
    """
    persons images component class.
    """
    pass
