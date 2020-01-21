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


class PermissionSubsystemCodeNotProvidedError(PermissionManagerException):
    """
    permission subsystem code not provided error.
    """
    pass


class PermissionSubsystemCodeLengthError(PermissionManagerException):
    """
    permission subsystem code length error.
    """
    pass


class PermissionAccessCodeNotProvidedError(PermissionManagerException):
    """
    permission access code not provided error.
    """
    pass


class InvalidPermissionAccessCodeError(PermissionManagerException):
    """
    invalid permission access code error.
    """
    pass


class PermissionSubAccessCodeNotProvidedError(PermissionManagerException):
    """
    permission sub access code not provided error.
    """
    pass


class InvalidPermissionSubAccessCodeError(PermissionManagerException):
    """
    invalid permission sub access code error.
    """
    pass


class PermissionDescriptionNotProvidedError(PermissionManagerException):
    """
    permission description not provided error.
    """
    pass


class PermissionDescriptionLengthError(PermissionManagerException):
    """
    permission description length error.
    """
    pass


class PermissionLocalizedDescriptionLengthError(PermissionManagerException):
    """
    permission localized description length error.
    """
    pass
