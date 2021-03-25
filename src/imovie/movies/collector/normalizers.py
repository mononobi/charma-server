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
        initializes an instance of AlreadyCollectedMovieNameNormalizer.
        """

        filters = ['[Indeterminate]', '[VCD]', '[DVD]', '[360p]',
                   '[480p]', '[720p]', '[1080p]', '[HD]', '[FHD]',
                   '[QHD]', '[UHD]', '[NA]', '[]', '()', '[', ']']

        filter_map = {'.': ' ', '_': ' '}
        options.update(filters=filters, filter_map=filter_map)

        super().__init__(MovieNormalizerEnum.MOVIE_NAME_METADATA, 90, **options)
