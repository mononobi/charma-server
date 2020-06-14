# -*- coding: utf-8 -*-
"""
validator base module.
"""

from pyrin.core.globals import _

from imovie.validator.exceptions import ValidationError
from imovie.validator.interface import AbstractValidatorBase
from imovie.validator.handlers.exceptions import ValidatorNameIsRequiredError, \
    ValueCouldNotBeNoneError, InvalidValueTypeError, InvalidValueError


class ValidatorBase(AbstractValidatorBase):
    """
    validator base class.

    all application validators must be subclassed from this.
    """

    # the accepted type for value.
    # if set to None, no type checking will be done.
    accepted_type = None
    invalid_type_error = InvalidValueTypeError
    invalid_type_message = _('The provided value for [{param_name}] '
                             'is not an instance of [{type}].')
    nullable = True
    none_value_error = ValueCouldNotBeNoneError
    none_value_message = _('The provided value for [{param_name}] could not be None.')

    def __init__(self, name):
        """
        initializes an instance of ValidatorBase.

        :param str name: validator name.
                         each validator will be registered with
                         its name in corresponding validator manager.
                         to enable automatic validations, the provided
                         name must be the exact name of the parameter
                         which this validator will validate.

        :raises ValidatorNameIsRequiredError: Validator Name Is Required Error.
        """

        if name in (None, '') or name.isspace():
            raise ValidatorNameIsRequiredError('Validator name must be provided.')

        super().__init__()
        self._set_name(name)

    def validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.

        :param object value: value to be validated.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises InvalidValueTypeError: invalid value type error.
        :raises InvalidValueError: invalid value error.
        :raises ValueCouldNotBeNoneError: value could not be none error.
        :raises ValidationError: validation error.
        """

        nullable = options.get('nullable', None) or self.nullable
        if nullable is None:
            nullable = True

        if value is not None:
            self._validate_type(value)
            try:
                self._validate(value, **options)
            except ValidationError as error:
                raise error
            except Exception:
                raise InvalidValueError(_('The provided value for '
                                          '[{param_name}] is invalid.').
                                        format(param_name=self.name))
        elif nullable is True:
            return
        else:
            raise self.none_value_error(
                self.none_value_message.format(param_name=self.name))

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        this method must be implemented in subclasses.
        each overridden method must call `super()._validate()`
        preferably at the beginning.
        if no extra validation is needed, it could be left unimplemented.

        :param object value: value to be validated.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValidationError: validation error.
        """
        pass

    def _validate_type(self, value):
        """
        validates the type of given value.

        if no accepted type is set for this validator, this method does nothing.

        :param object value: value to be validated.

        :raises InvalidValueTypeError: invalid value type error.
        """

        if self.accepted_type is None:
            return

        if not isinstance(value, self.accepted_type):
            raise self.invalid_type_error(self.invalid_type_message.format(
                param_name=self.name, type=self.accepted_type))

    @property
    def name(self):
        """
        gets the name of this validator.

        :rtype: str
        """

        return self.get_name()
