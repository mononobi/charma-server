# -*- coding: utf-8 -*-
"""
actors hooks module.
"""

from pyrin.core.structs import Hook


class ActorHookBase(Hook):
    """
    actor hook base class.

    all packages that need to be hooked in actors business, must implement
    this class and register an instance of it in actor hooks.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever an actor is going to be deleted.

        :param uuid.UUID id: person id.
        """
        pass
