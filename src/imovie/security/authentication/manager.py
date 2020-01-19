# -*- coding: utf-8 -*-
"""
authentication manager module.
"""

import pyrin.security.session.services as session_services

from pyrin.security.authentication.exceptions import AuthenticationFailedError
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
        :type payload: dict(str type: token type,
                            int user_id: user id)

        :raises InvalidUserError: invalid user error.
        :raises CouldNotOverwriteCurrentUserError: could not overwrite current user error.
        """

        user_id = payload.pop('user_id')
        session_services.set_current_user(user_id)

    def _validate_custom(self, header, payload, **options):
        """
        validates the given inputs for custom attributes.
        an error will be raised if validation fails.

        :param dict header: token header data.

        :param dict payload: payload data to be validated.
        :type payload: dict(str type: token type,
                            int user_id: user id)

        :raises AuthenticationFailedError: authentication failed error.
        """

        user_id = payload.get('user_id', None)
        if user_id is None:
            raise AuthenticationFailedError('User id must be provided in payload.')
