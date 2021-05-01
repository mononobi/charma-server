# -*- coding: utf-8 -*-
"""
search providers mixins module.
"""

import re

from pyrin.core.structs import CoreObject


class IMDBMovieMixin(CoreObject):
    """
    imdb movie mixin class.
    """

    _target = 'imdb'
    _category = 'movie'
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?imdb\.com/title/[^/]+).*$',
                                          re.IGNORECASE)


class SubsceneMixin(CoreObject):
    """
    subscene mixin class.
    """

    _target = 'subscene'
    _category = 'subtitle'
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?subscene\.com/subtitles/[^/]+).*$',
                                          re.IGNORECASE)
