# -*- coding: utf-8 -*-
"""
updater component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.updater import UpdaterPackage
from charma.updater.manager import UpdaterManager


@component(UpdaterPackage.COMPONENT_NAME)
class UpdaterComponent(Component, UpdaterManager):
    """
    updater component class.
    """
    pass
