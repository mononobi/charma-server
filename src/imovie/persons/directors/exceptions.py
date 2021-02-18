# -*- coding: utf-8 -*-
"""
directors exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class DirectorsException(CoreException):
    """
    directors exception.
    """
    pass


class DirectorsBusinessException(CoreBusinessException, DirectorsException):
    """
    directors business exception.
    """
    pass


class DirectorDoesNotExistError(DirectorsBusinessException):
    """
    director does not exist error.
    """
    pass
