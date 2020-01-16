# -*- coding: utf-8 -*-
"""
permission base module.
"""

from pyrin.security.permission.base import PermissionBase


class CorePermission(PermissionBase):
    """
    core permission class.
    all application permissions must be subclassed from this.
    """

    def __init__(self, permission_id, description, **options):
        """
        initializes an instance of PermissionBase.

        :param object permission_id: permission id.
                                     it must be an immutable type to
                                     be usable as dict key.

        :param str description: permission description.
        """

        PermissionBase.__init__(self, permission_id, description, **options)

    def __hash__(self):
        """
        this method must be implemented in all subclasses to
        calculate the correct hash of current permission.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: int
        """

        return id(self)

    def __str__(self):
        """
        this method must be implemented in all subclasses to
        get the correct string representation of current permission.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        return self.get_name()

    def get_id(self):
        """
        gets permission id.
        it must be an immutable type to be usable as dict key.

        :rtype: object
        """

        return self._id

    def synchronize(self, **options):
        """
        synchronizes the current permission object with database.

        :raises CoreNotImplementedError: core not implemented error.
        """

        return
