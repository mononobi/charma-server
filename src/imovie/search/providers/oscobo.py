# -*- coding: utf-8 -*-
"""
search providers oscobo module.
"""

import re

from imovie.search.decorators import search_provider
from imovie.search.providers.base import SearchProviderBase


class OscoboBase(SearchProviderBase):
    """
    oscobo base class.
    """

    _name = 'oscobo'
    _remote_url = 'https://www.oscobo.com/search.php?q={query}'


@search_provider()
class OscoboMovieProvider(OscoboBase):
    """
    oscobo movie provider class.
    """

    _category = 'movie'
    _accepted_result_pattern = re.compile(r'^(https://imdb\.com/title/[^/]+).*$',
                                          re.IGNORECASE)

    def _prepare_url(self, url):
        """
        prepares given matched url to be returned by this provider.

        subclasses could override this if needed.

        :param str url: url to be prepared.

        :rtype: str
        """

        return url

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if noting found.

        :param str response: html response.

        :rtype: list[str]
        """

        return []


@search_provider()
class OscoboSubtitleProvider(OscoboBase):
    """
    oscobo subtitle provider class.
    """

    _category = 'subtitle'
    _accepted_result_pattern = re.compile(r'^(https://subscene\.com/subtitles/[^/]+).*$',
                                          re.IGNORECASE)

    def _prepare_url(self, url):
        """
        prepares given matched url to be returned by this provider.

        subclasses could override this if needed.

        :param str url: url to be prepared.

        :rtype: str
        """

        return url

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if noting found.

        :param str response: html response.

        :rtype: list[str]
        """

        return []
