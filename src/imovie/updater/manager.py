# -*- coding: utf-8 -*-
"""
updater manager module.
"""

from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from imovie.updater import UpdaterPackage


class UpdaterManager(Manager):
    """
    updater manager class.
    """

    package_class = UpdaterPackage
