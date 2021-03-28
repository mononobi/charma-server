# -*- coding: utf-8 -*-
"""
movies collector enumerations module.
"""

from pyrin.core.enumerations import CoreEnum


class MovieNormalizerEnum(CoreEnum):
    """
    movie normalizer enum.
    """

    MOVIE_NAME_METADATA = 'movie_name_metadata'
    MOVIE_COUNTING_LETTER = 'movie_counting_letter'
    MOVIE_SEQUENCE_SLUG = 'movie_sequence_slug'
