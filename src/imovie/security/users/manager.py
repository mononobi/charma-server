# -*- coding: utf-8 -*-
"""
users manager module.
"""

import pyrin.utils.sqlalchemy as sqlalchemy_utils

from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import entity_to_dict
from pyrin.core.globals import _
from pyrin.security.users.manager import UsersManager as BaseUsersManager

from imovie.security.users.exceptions import UserNotFoundError, InvalidUserError


class UsersManager(BaseUsersManager):
    """
    users manager class.
    """

    def get(self, user_id, **options):
        """
        gets the specified user.

        :param int user_id: user id to get its info.

        :raises UserNotFoundError: user not found error.

        :returns: dict(int id,
                       int portal_code,
                       int person_type,
                       str first_name,
                       str last_name,
                       int gender,
                       str national_code,
                       str mobile_number1,
                       str phone_number1,
                       str address,
                       str zip_code,
                       str email,
                       datetime registration_date,
                       datetime activation_date,
                       bool deleted,
                       str description,
                       bool active,
                       str about,
                       date birth_date,
                       int country_id,
                       int default_mobile,
                       bool is_customer,
                       datetime edited_date,
                       int category_id,
                       int registrar_id,
                       int editor_id,
                       int province_id,
                       int city_id,
                       str username,
                       str password,
                       bool pos_default,
                       int hamdige_source_portal_code,
                       str hamdige_nickname,
                       str card_number,
                       str iban_number)

        :note person_type:
            UNKNOWN = 0
            REAL = 1
            LEGAL = 2

        :note gender:
            UNKNOWN = 0
            FEMALE = 1
            MALE = 2

        :note default_mobile:
            ONE = 1
            TWO = 2
            THREE = 3
            FOUR = 4

        :rtype: dict
        """

        store = get_current_store()
        user = store.query().get(user_id)

        if user is None:
            raise UserNotFoundError(_('User [{user_id}] not found.'.format(user_id=user_id)))

        return entity_to_dict(user)

    def _user_exists(self, user):
        """
        gets a value indicating that given user existed.

        :param dict user: user identity to check for existence.
        :type user: dict(int user_id,
                         int portal_code)

        :raises InvalidUserError: invalid user error.

        :rtype: bool
        """

        if user is None:
            raise InvalidUserError(_('Input user could not be None.'))

        store = get_current_store()
        query = store.query().filter()

        user_count = sqlalchemy_utils.count(query)
        return user_count > 0

    def is_active(self, user, **options):
        """
        gets a value indicating that given user is active.

        :param dict user: user to check its active status.

        :type user: dict(int user_id: user id,
                         int portal_code: portal code)

        :raises InvalidUserError: invalid user error.
        :raises UserNotFoundError: user not found error.

        :rtype: bool
        """

        if self._user_exists(user) is not True:
            raise UserNotFoundError(_('User [{user}] not found.').format(user=user))

        store = get_current_store()
        user_info = self.get(user.user_id)

        return user_info.active

    def create(self, username, password, mobile_number, **options):
        """

        :param str username: username.
        :param str password: password.
        :param str mobile_number: mobile number.

        :returns: created user id.

        :rtype: int
        """
