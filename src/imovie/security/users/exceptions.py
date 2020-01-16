# -*- coding: utf-8 -*-
"""
users exceptions module.
"""

from pyrin.core.exceptions import CoreBusinessException, CoreException


class UsersManagerException(CoreException):
    """
    users manager exception.
    """
    pass


class UsersManagerBusinessException(CoreBusinessException,
                                    UsersManagerException):
    """
    users manager business exception.
    """
    pass


class InvalidUserError(UsersManagerBusinessException):
    """
    invalid user error.
    """
    pass


class UserNotFoundError(UsersManagerBusinessException):
    """
    user not found error.
    """
    pass
