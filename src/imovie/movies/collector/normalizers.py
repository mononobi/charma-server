# -*- coding: utf-8 -*-
"""
movies collector normalizers module.
"""

from pyrin.utilities.string.normalizer.decorators import string_normalizer
from pyrin.utilities.string.normalizer.handlers.base import FilterNormalizerBase

from imovie.movies.collector.enumerations import MovieNormalizerEnum


@string_normalizer()
class MovieNameMetadataNormalizer(FilterNormalizerBase):
    """
    movie name metadata normalizer class.

    this normalizer removes all metadata values from already collected movie names.
    """

    def __init__(self, **options):
        """
        initializes an instance of MovieNameMetadataNormalizer.
        """

        filters = ['\\[Indeterminate]', '\\[VCD]', '\\[DVD]', '\\[360p]',
                   '\\[480p]', '\\[720p]', '\\[1080p]', '\\[HD]', '\\[FHD]',
                   '\\[QHD]', '\\[UHD]', '\\[NA]', '\\[]', '\\(\\)', '\\[',
                   ']', '\\{}', 'beginslug[0-9]{4}endslug$']

        filter_map = {'\\.': ' ', '_': ' '}
        options.update(filters=filters, filter_map=filter_map)

        super().__init__(MovieNormalizerEnum.MOVIE_NAME_METADATA, 90, **options)


@string_normalizer()
class CountingLetterNormalizer(FilterNormalizerBase):
    """
    counting letter normalizer.

    this normalizer makes all counting letters lowercase.
    for example: 1st, 2nd, 3rd, 4th.
    """

    def __init__(self, **options):
        """
        initializes an instance of CountingLetterNormalizer.
        """

        filter_map = {'([0-9]+)st': '\\1st', '([0-9]+)nd': '\\1nd',
                      '([0-9]+)rd': '\\1rd', '([0-9]+)th': '\\1th'}

        options.update(filter_map=filter_map)

        super().__init__(MovieNormalizerEnum.MOVIE_COUNTING_LETTER, 91, **options)


@string_normalizer()
class MovieNameSequenceSlugNormalizer(FilterNormalizerBase):
    """
    movie name sequence slug normalizer class.

    this normalizer removes sequence slug from movie name.
    """

    def __init__(self, **options):
        """
        initializes an instance of MovieNameSequenceSlugNormalizer.
        """

        filters = [' -D[0-9]{2}$']
        options.update(filters=filters)

        super().__init__(MovieNormalizerEnum.MOVIE_SEQUENCE_SLUG, 92, **options)
