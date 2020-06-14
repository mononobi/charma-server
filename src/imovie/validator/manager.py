# -*- coding: utf-8 -*-
"""
validator manager module.
"""

from pyrin.core.structs import Manager, Context
from pyrin.utils.custom_print import print_warning

from imovie.validator.exceptions import InvalidValidatorTypeError, DuplicatedValidatorError, \
    ValidatorNotFoundError
from imovie.validator.interface import AbstractValidatorBase


class ValidatorManager(Manager):
    """
    validator manager class.
    """

    def __init__(self):
        """
        initializes an instance of ValidatorManager.
        """

        super().__init__()

        # a dictionary containing information of registered validators.
        # example: dic(str name: AbstractValidatorBase instance)
        self._validators = Context()

    def register_validator(self, instance, **options):
        """
        registers a new validator or replaces the existing one.

        if `replace=True` is provided. otherwise, it raises an error
        on adding a validator which is already registered.

        :param AbstractValidatorBase instance: validator to be registered.
                                               it must be an instance of
                                               AbstractValidatorBase.

        :keyword bool replace: specifies that if there is another registered
                               validator with the same name, replace it with
                               the new one, otherwise raise an error.
                               defaults to False.

        :raises InvalidValidatorTypeError: invalid validator type error.
        :raises DuplicatedValidatorError: duplicated validator error.
        """

        if not isinstance(instance, AbstractValidatorBase):
            raise InvalidValidatorTypeError('Input parameter [{instance}] is '
                                            'not an instance of [{base}].'
                                            .format(instance=instance,
                                                    base=AbstractValidatorBase))

        if instance.name in self._validators:
            old_instance = self.get_validator(instance.name)
            replace = options.get('replace', False)
            if replace is not True:
                raise DuplicatedValidatorError('There is another registered '
                                               'validator [{old}] with name '
                                               '[{name}] but "replace" option '
                                               'is not set, so validator [{instance}] '
                                               'could not be registered.'
                                               .format(old=old_instance,
                                                       name=instance.name,
                                                       instance=instance))

            print_warning('Validator [{old_instance}] is going '
                          'to be replaced by [{new_instance}].'
                          .format(old_instance=old_instance,
                                  new_instance=instance))

        self._validators[instance.name] = instance

    def get_validator(self, name):
        """
        gets the registered validator with given name.

        it returns None if no validator found for given name.

        :param str name: validator name to get.

        :rtype: AbstractValidatorBase
        """

        return self._validators.get(name, None)

    def validate_field(self, name, value, **options):
        """
        validates the given value with given validator.

        :param str name: validator name to be used for validation.
        :param object value: value to be validated.

        :keyword bool force: specifies that if there is no validator
                             with given name, it should raise an error.
                             defaults to False if not provided.

        :keyword bool nullable: determines that provided value could be None.

        :keyword bool inclusive_minimum: determines that values equal to
                                         accepted minimum should be considered valid.

        :keyword bool inclusive_maximum: determines that values equal to
                                         accepted maximum should be considered valid.

        :raises ValidatorNotFoundError: validator not found error.
        :raises ValidationError: validation error.
        """

        validator = self.get_validator(name)
        force = options.get('force', None)
        if force is None:
            force = False

        if force is not False and validator is None:
            raise ValidatorNotFoundError('There is no validator with name [{name}].'
                                         .format(name=name))

        if validator is not None:
            validator.validate(value, **options)

    def validate_dict(self, data, **options):
        """
        validates available values of given dict.

        it uses the correct validator for each value based on its key name.

        :param dict data: dictionary to validate its values.

        :keyword bool force: specifies that if there is no validator
                             for any of key names, it should raise an error.
                             defaults to False if not provided.

        :keyword bool nullable: determines that provided values could be None.

        :keyword bool inclusive_minimum: determines that values equal to
                                         accepted minimum should be considered valid.

        :keyword bool inclusive_maximum: determines that values equal to
                                         accepted maximum should be considered valid.

        :raises ValidatorNotFoundError: validator not found error.
        :raises ValidationError: validation error.
        """

        if data is not None:
            for name, value in data.items():
                self.validate_field(name, value, **options)
