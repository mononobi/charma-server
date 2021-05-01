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
    _remote_url = 'https://www.oscobo.com/search.php?q={query} {target}'

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param BeautifulSoup response: html response.

        :rtype: list[str]
        """

        urls = []
        result_list = response.find('div', id='results-list')
        results = result_list.find_all('div', class_='line cite')
        for item in results:
            urls.append(item.get_text(strip=True))

        return urls


@search_provider()
class OscoboIMDBProvider(OscoboBase):
    """
    oscobo imdb provider class.
    """

    _target = 'imdb'
    _category = 'movie'
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?imdb\.com/title/[^/]+).*$',
                                          re.IGNORECASE)


@search_provider()
class OscoboSubsceneProvider(OscoboBase):
    """
    oscobo subscene provider class.
    """

    _target = 'subscene'
    _category = 'subtitle'
    _accepted_result_pattern = re.compile(r'^(https?://(www\.)?subscene\.com/subtitles/[^/]+).*$',
                                          re.IGNORECASE)
