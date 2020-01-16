# -*- coding: utf-8 -*-
"""
security manager module.
"""

from pyrin.security.manager import SecurityManager as BaseSecurityManager


class SecurityManager(BaseSecurityManager):
    """
    security manager class.
    """

    def get_permission_ids(self, **options):
        """
        gets permission ids according to given inputs.

        :keyword dict user: user identity to get it's permission ids.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: list[permission_ids]

        :rtype: list[object]
        """

        return []
