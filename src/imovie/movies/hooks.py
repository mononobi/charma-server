# -*- coding: utf-8 -*-
"""
movies hooks module.
"""

from pyrin.core.structs import Hook


class MovieHookBase(Hook):
    """
    movie hook base class.

    all packages that need to be hooked in movie business, must implement
    this class and register an instance of it in movie hooks.
    """

    def delete(self, id):
        """
        deletes a movie with given id.

        :param uuid.UUID id: movie id.
        """
        pass
