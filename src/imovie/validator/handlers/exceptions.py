# -*- coding: utf-8 -*-
"""
validator handlers exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException

from imovie.validator.exceptions import ValidationError


class ValidatorHandlersException(CoreException):
    """
    validator handlers exception.
    """
    pass


class ValidatorHandlersBusinessException(CoreBusinessException,
                                         ValidatorHandlersException):
    """
    validator handlers business exception.
    """
    pass


class ValidatorNameIsRequiredError(ValidatorHandlersException):
    """
    validator name is required error.
    """
    pass


class ValueCouldNotBeNoneError(ValidatorHandlersBusinessException,
                               ValidationError):
    """
    value could not be none error.
    """
    pass


class ValueIsLowerThanMinimumError(ValidatorHandlersBusinessException,
                                   ValidationError):
    """
    value is lower than minimum error.
    """
    pass


class ValueIsHigherThanMaximumError(ValidatorHandlersBusinessException,
                                    ValidationError):
    """
    value is higher than maximum error.
    """
    pass


class ValueIsOutOfRangeError(ValidatorHandlersBusinessException,
                             ValidationError):
    """
    value is out of range error.
    """
    pass


class InvalidValueTypeError(ValidatorHandlersBusinessException,
                            ValidationError):
    """
    invalid value type error.
    """
    pass


class InvalidValueError(ValidatorHandlersBusinessException,
                        ValidationError):
    """
    invalid value error.
    """
    pass


class ValueDoesNotMatchPatternError(ValidatorHandlersBusinessException,
                                    ValidationError):
    """
    value does not match pattern error.
    """
    pass
