# -*- coding: utf-8 -*-
"""
validator interface module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError
from pyrin.core.structs import CoreObject


class AbstractValidatorBase(CoreObject):
    """
    abstract validator base class.

    all application validators must be subclassed from this.
    """

    @abstractmethod
    def validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.

        :param object value: value to be validated.

        :raises CoreNotImplementedError: core not implemented error.
        :raises ValidationError: validation error.
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def name(self):
        """
        gets the name of this validator.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()
