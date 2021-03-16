# -*- coding: utf-8 -*-
"""
common normalizer mixin module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.structs import CoreObject
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum


class NormalizerMixin(CoreObject):
    """
    normalizer mixin class.
    """

    NORMALIZERS = [NormalizerEnum.PERSIAN_SIGN,
                   NormalizerEnum.LATIN_SIGN,
                   NormalizerEnum.PERSIAN_NUMBER,
                   NormalizerEnum.ARABIC_NUMBER,
                   NormalizerEnum.PERSIAN_LETTER,
                   NormalizerEnum.LATIN_LETTER,
                   NormalizerEnum.LOWERCASE,
                   NormalizerEnum.SPACE]

    def get_normalized(self, value, **options):
        """
        gets normalized value from given value.

        :param str value: value to be normalized.

        :keyword list[str] filters: list of items to be removed from string.
                                    defaults to None. it will only be used
                                    for `filter` normalizer.

        :keyword bool ignore_case: remove `filters` from string in case-insensitive
                                   way. defaults to True if not provided.

        :keyword bool strip: strip spaces from both ends of string on each
                             normalization step. defaults to True if not provided.

        :keyword bool normalize_none: specifies that if given value is None,
                                      return empty string instead of None.
                                      defaults to False if not provided.

        :rtype: str
        """

        return normalizer_services.normalize(value, *self.NORMALIZERS, **options)
