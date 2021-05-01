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

    _remote_url = 'https://www.oscobo.com/search.php?q={query}'

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param BeautifulSoup response: html response.

        :rtype: list[str]
        """

        urls = []
        results = response.find_all('div', class_='line cite')
        for item in results:
            urls.append(item.get_text(strip=True))

        return urls


@search_provider()
class OscoboIMDBProvider(OscoboBase):
    """
    oscobo imdb provider class.
    """

    _name = 'oscobo.imdb'
    _category = 'movie'
    _accepted_result_pattern = re.compile(r'^(https://www\.imdb\.com/title/[^/]+).*$',
                                          re.IGNORECASE)


@search_provider()
class OscoboSubsceneProvider(OscoboBase):
    """
    oscobo subscene provider class.
    """

    _name = 'oscobo.subscene'
    _category = 'subtitle'
    _accepted_result_pattern = re.compile(r'^(https://www\.subscene\.com/subtitles/[^/]+).*$',
                                          re.IGNORECASE)
