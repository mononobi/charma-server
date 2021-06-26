# -*- coding: utf-8 -*-
"""
authentication manager module.
"""

from pyrin.core.exceptions import CoreNotImplementedError
from pyrin.security.authentication.manager import AuthenticationManager as \
    BaseAuthenticationManager


class AuthenticationManager(BaseAuthenticationManager):
    """
    authentication manager class.
    """

    def _push_custom_data(self, header, payload, **options):
        """
        pushes the custom data into current request from input values.

        :param dict header: token header data.
        :param dict payload: payload data of authenticated token.
        """

        raise CoreNotImplementedError()

    def _validate_custom(self, header, payload, **options):
        """
        validates the given inputs for custom attributes.

        an error will be raised if validation fails.

        :param dict header: token header data.
        :param dict payload: payload data to be validated.

        :raises AuthenticationFailedError: authentication failed error.
        """

        raise CoreNotImplementedError()
