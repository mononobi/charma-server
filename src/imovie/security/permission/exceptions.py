# -*- coding: utf-8 -*-
"""
permission exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class PermissionManagerException(CoreException):
    """
    permission manager exception.
    """
    pass


class PermissionManagerBusinessException(CoreBusinessException,
                                         PermissionManagerException):
    """
    permission manager business exception.
    """
    pass


class InvalidPermissionSubsystemCodeError(PermissionManagerException):
    """
    invalid permission subsystem code error.
    """
    pass


class InvalidPermissionAccessCodeError(PermissionManagerException):
    """
    invalid permission access code error.
    """
    pass


class InvalidPermissionSubAccessCodeError(PermissionManagerException):
    """
    invalid permission sub access code error.
    """
    pass


class InvalidPermissionDescriptionError(PermissionManagerException):
    """
    invalid permission description error.
    """
    pass
