# -*- coding: utf-8 -*-
"""
search providers mixin module.
"""

import re

from pyrin.core.structs import CoreObject

from imovie.search.enumerations import SearchCategoryEnum


class IMDBMovieMixin(CoreObject):
    """
    imdb movie mixin class.
    """

    _target = 'imdb'
    _category = SearchCategoryEnum.MOVIE
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?imdb\.com/title/[^/]+).*$',
                                          re.IGNORECASE)


class SubsceneMixin(CoreObject):
    """
    subscene mixin class.
    """

    _target = 'subscene'
    _category = SearchCategoryEnum.SUBTITLE
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?subscene\.com/subtitles/[^/]+).*$',
                                          re.IGNORECASE)
