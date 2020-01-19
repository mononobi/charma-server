# -*- coding: utf-8 -*-
"""
permission base module.
"""

from pyrin.security.permission.base import PermissionBase


class CorePermission(PermissionBase):
    """
    core permission class.
    all application permissions must be an instance of this class.
    """

    def __init__(self, subsystem_code, transaction_code, sub_transaction_code,
                 description, locale_description, **options):
        """
        initializes an instance of CorePermission.

        :param str subsystem_code: subsystem code.
        :param int access_code:
        :param sub_access_code:
        :param description:
        :param locale_description:
        :param options:
        """
        PermissionBase.__init__(self, subsystem_code, transaction_code,
                                sub_transaction_code, description,
                                locale_description, **options)

    def __hash__(self):
        """
        this method must be implemented in all subclasses to
        calculate the correct hash of current permission.

        :rtype: int
        """

        return id(self)

    def __str__(self):
        """
        this method must be implemented in all subclasses to
        get the correct string representation of current permission.

        :rtype: str
        """

        return self.get_name()

    def __repr__(self):
        """
        this method must be implemented in all subclasses to
        get the correct string representation of current permission.

        :rtype: str
        :return:
        """
        pass

    def get_id(self):
        """
        gets permission id.
        it must be an immutable type to be usable as dict key.

        :rtype: object
        """

        return 1

    def synchronize(self, **options):
        """
        synchronizes the current permission object with database.
        """

        return
