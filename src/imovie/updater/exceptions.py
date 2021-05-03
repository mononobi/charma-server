# -*- coding: utf-8 -*-
"""
updater exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class UpdaterException(CoreException):
    """
    updater exception.
    """
    pass


class UpdaterBusinessException(CoreBusinessException, UpdaterException):
    """
    updater business exception.
    """
    pass


class InvalidUpdaterTypeError(UpdaterException):
    """
    invalid updater type error.
    """
    pass


class DuplicateUpdaterError(UpdaterException):
    """
    duplicate updater error.
    """
    pass
