# -*- coding: utf-8 -*-
"""
validator handlers mixin module.
"""

from pyrin.core.globals import _

from imovie.validator.exceptions import ValidationError
from imovie.validator.handlers.base import ValidatorBase
from imovie.validator.handlers.exceptions import ValueIsLowerThanMinimumError, \
    ValueIsHigherThanMaximumError, ValueIsOutOfRangeError, ValueDoesNotMatchPatternError


class MinimumValidatorMixin(ValidatorBase):
    """
    minimum validator mixin class.
    """

    accepted_minimum = None
    inclusive_minimum = True
    minimum_value_error = ValueIsLowerThanMinimumError
    minimum_value_message = _('The provided value for [{param_name}] is lower than '
                              'the accepted minimum value, which is [{minimum}].')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool inclusive_minimum: determines that values equal to
                                         accepted minimum should be considered valid.
                                         this value has precedence over `inclusive_minimum`
                                         class attribute if provided.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueIsLowerThanMinimumError: value is lower than minimum error.
        """

        super()._validate(value, **options)

        inclusive_minimum = options.get('inclusive_minimum', None) or self.inclusive_minimum
        if inclusive_minimum is None:
            inclusive_minimum = True

        if value < self.accepted_minimum or \
                (value == self.accepted_minimum and inclusive_minimum is not True):
            raise self.minimum_value_error(
                self.minimum_value_message.format(param_name=self.name,
                                                  minimum=self.accepted_minimum))


class MaximumValidatorMixin(ValidatorBase):
    """
    maximum validator mixin class.
    """

    accepted_maximum = None
    inclusive_maximum = True
    maximum_value_error = ValueIsHigherThanMaximumError
    maximum_value_message = _('The provided value for [{param_name}] is higher than '
                              'the accepted maximum value, which is [{maximum}].')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool inclusive_maximum: determines that values equal to
                                         accepted maximum should be considered valid.
                                         this value has precedence over `inclusive_maximum`
                                         class attribute if provided.


        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueIsHigherThanMaximumError: value is higher than maximum error.
        """

        super()._validate(value, **options)

        inclusive_maximum = options.get('inclusive_maximum', None) or self.inclusive_maximum
        if inclusive_maximum is None:
            inclusive_maximum = True

        if value > self.accepted_maximum or \
                (value == self.accepted_maximum and inclusive_maximum is not True):
            raise self.maximum_value_error(
                self.maximum_value_message.format(param_name=self.name,
                                                  maximum=self.accepted_maximum))


class RangeValidatorMixin(MinimumValidatorMixin, MaximumValidatorMixin):
    """
    range validator mixin class.
    """

    range_value_error = ValueIsOutOfRangeError
    range_value_message = _('The provided value for [{param_name}] must '
                            'be between [{lower}] and [{upper}].')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool inclusive_minimum: determines that values equal to
                                         accepted minimum should be considered valid.
                                         this value has precedence over `inclusive_minimum`
                                         class attribute if provided.

        :keyword bool inclusive_maximum: determines that values equal to
                                         accepted maximum should be considered valid.
                                         this value has precedence over `inclusive_maximum`
                                         class attribute if provided.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueIsOutOfRangeError: value is out of range error.
        """

        try:
            super()._validate(value, **options)
        except ValidationError:
            raise self.range_value_error(self.range_value_message.format(
                lower=self.accepted_minimum, upper=self.accepted_maximum))


class InValidatorMixin(ValidatorBase):
    """
    in validator mixin class.
    """

    accepted_values = []
    not_in_value_error = ValueIsOutOfRangeError
    not_in_value_message = _('The provided value for [{param_name}] '
                             'must be from [{values}].')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueIsOutOfRangeError: value is out of range error.
        """

        super()._validate(value, **options)

        if value not in self.accepted_values:
            raise self.not_in_value_error(self.not_in_value_message.format(
                param_name=self.name, values=self.accepted_values))


class NotInValidatorMixin(ValidatorBase):
    """
    not in validator mixin class.
    """

    excluded_values = []
    in_value_error = ValueIsOutOfRangeError
    in_value_message = _('The provided value for [{param_name}] '
                         'could not be from [{values}].')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueIsOutOfRangeError: value is out of range error.
        """

        super()._validate(value, **options)

        if value in self.excluded_values:
            raise self.in_value_error(self.in_value_message.format(
                param_name=self.name, values=self.excluded_values))


class RegexValidatorMixin(ValidatorBase):
    """
    regex validator mixin class.
    """

    accepted_type = str
    regex = None
    not_match_pattern_error = ValueDoesNotMatchPatternError
    not_match_pattern_message = _('The provided value for [{param_name}] '
                                  'does not match the required pattern.')

    def _validate(self, value, **options):
        """
        validates the given value.

        it raises an error if validation fails.
        the raised error must be an instance of ValidationError.
        each overridden method must call `super()._validate()`
        preferably at the beginning.

        :param object value: value to be validated.

        :keyword bool nullable: determines that provided value could be None.
                                this value has precedence over `nullable`
                                class attribute if provided.

        :raises ValueDoesNotMatchPatternError: value does not match pattern error.
        """

        super()._validate(value, **options)

        if not self.regex.match(value):
            raise self.not_match_pattern_error(
                self.not_match_pattern_message.format(param_name=self.name))
