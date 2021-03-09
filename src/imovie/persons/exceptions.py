# -*- coding: utf-8 -*-
"""
persons exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class PersonsException(CoreException):
    """
    persons exception.
    """
    pass


class PersonsBusinessException(CoreBusinessException, PersonsException):
    """
    persons business exception.
    """
    pass


class PersonDoesNotExistError(PersonsBusinessException):
    """
    person does not exist error.
    """
    pass


class InvalidPersonHandlerTypeError(PersonsException):
    """
    invalid person handler type error.
    """
    pass


class PersonHandlerNameRequiredError(PersonsException):
    """
    person handler name required error.
    """
    pass


class DuplicatedPersonHandlerError(PersonsException):
    """
    duplicated person handler error.
    """
    pass


class PersonHandlerNotExistedError(PersonsBusinessException):
    """
    person handler not existed error.
    """
    pass


class InvalidPersonHookTypeError(PersonsException):
    """
    invalid person hook type error.
    """
    pass
