# -*- coding: utf-8 -*-
"""
countries component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.countries import CountriesPackage
from charma.countries.manager import CountriesManager


@component(CountriesPackage.COMPONENT_NAME)
class CountriesComponent(Component, CountriesManager):
    """
    countries component class.
    """
    pass
