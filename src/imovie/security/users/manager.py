# -*- coding: utf-8 -*-
"""
users manager module.
"""

import pyrin.utils.sqlalchemy as sqlalchemy_utils
import pyrin.security.services as security_services
import pyrin.globalization.datetime.services as datetime_services

from pyrin.security.session.services import get_current_user
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import entity_to_dict
from pyrin.core.globals import _
from pyrin.security.users.manager import UsersManager as BaseUsersManager
from pyrin.utils.unique_id import generate_uuid4

from imovie.security.users.models import UserEntity
from imovie.security.users.exceptions import UserNotFoundError, InvalidUserError


class UsersManager(BaseUsersManager):
    """
    users manager class.
    """

    def _get(self, user_id=None):
        """
        gets specified user info.

        :param str user_id: user id to get its info.
                            if not provided, current user
                            info will be fetched.

        :raises UserNotFoundError: user not found error.

        :rtype: UserEntity
        """

        if user_id is None:
            user_id = get_current_user()

        store = get_current_store()
        user = store.query(UserEntity).get(user_id)

        if user is None:
            raise UserNotFoundError(_('User [{user_id}] not found.'.format(user_id=user_id)))

        return user

    def get(self):
        """
        gets current user info.

        :raises UserNotFoundError: user not found error.

        :returns: dict(str id,
                       str user_name,
                       str first_name,
                       str last_name,
                       str email,
                       datetime create_date,
                       int status,
                       datetime last_login_date,
                       int wrong_password_count)

        :note status:
            NOT_APPROVED = 0
            ACTIVE = 1
            SUSPENDED = 2
            DELETED = 3

        :rtype: dict
        """

        user = self._get()
        return entity_to_dict(user)

    def get_internal(self, user_id=None):
        """
        gets specified user info.

        :param str user_id: user id to get its info.
                            if not provided, current user
                            info will be fetched.

        :raises UserNotFoundError: user not found error.

        :rtype: UserEntity
        """

        user = self._get(user_id)
        return entity_to_dict(user)

    def _exists(self, user_id):
        """
        gets a value indicating that given user existed.

        :param str user_id: user id to check for existence.

        :raises InvalidUserError: invalid user error.

        :rtype: bool
        """

        if user_id is None:
            raise InvalidUserError(_('Input user could not be None.'))

        store = get_current_store()
        query = store.query(UserEntity.id).filter(UserEntity.id == user_id)
        user_count = sqlalchemy_utils.count(query, UserEntity.id)

        return user_count > 0

    def is_active(self, user_id, **options):
        """
        gets a value indicating that given user is active.

        :param str user_id: user id to check its status.

        :raises UserNotFoundError: user not found error.

        :rtype: bool
        """

        user = self.get_internal(user_id)
        return user.status == UserEntity.StatusEnum.ACTIVE

    def _create(self, username, password, first_name, last_name, email, **options):
        """
        creates a user with given inputs.

        :param str username: username.
        :param str password: password.
        :param str first_name: first name.
        :param str last_name: last name.
        :param str email: email.

        :returns: created user id.
        :rtype: str
        """

        entity = UserEntity()
        entity.id = generate_uuid4()
        entity.username = username
        entity.password_hash = security_services.get_password_hash(password)
        entity.first_name = first_name
        entity.last_name = last_name
        entity.email = email
        entity.status = UserEntity.StatusEnum.ACTIVE
        entity.create_date = datetime_services.now()

        self.validate(entity)

        store = get_current_store()
        store.add(entity)

        return entity.id

    def create(self, username, password, first_name, last_name, email, **options):
        """
        creates a user with given inputs.

        :param str username: username.
        :param str password: password.
        :param str first_name: first name.
        :param str last_name: last name.
        :param str email: email.

        :returns: created user id.
        :rtype: str
        """

        return self._create(username, password, first_name, last_name, email, **options)

    def validate(self, entity):
        """
        validates given user entity.

        :param UserEntity entity: user entity to be validated.
        """
        pass
