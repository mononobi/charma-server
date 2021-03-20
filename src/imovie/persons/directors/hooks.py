# -*- coding: utf-8 -*-
"""
directors hooks module.
"""

from pyrin.core.structs import Hook


class DirectorHookBase(Hook):
    """
    director hook base class.

    all packages that need to be hooked in directors business, must implement
    this class and register an instance of it in director hooks.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a director is going to be deleted.

        :param uuid.UUID id: person id.
        """
        pass
