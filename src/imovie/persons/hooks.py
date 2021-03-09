# -*- coding: utf-8 -*-
"""
persons hooks module.
"""

from pyrin.core.structs import Hook


class PersonHookBase(Hook):
    """
    person hook base class.

    all packages that need to be hooked in persons business, must implement
    this class and register an instance of it in person hooks.
    """

    def before_delete(self, id):
        """
        this method will be get called whenever a person is going to be deleted.

        :param uuid.UUID id: person id.
        """
        pass
