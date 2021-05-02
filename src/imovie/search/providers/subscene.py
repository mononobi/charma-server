# -*- coding: utf-8 -*-
"""
search providers subscene module.
"""

import re

from imovie.search.decorators import search_provider
from imovie.search.providers.base import SearchProviderBase


@search_provider()
class SubsceneProvider(SearchProviderBase):
    """
    subscene base class.
    """

    _name = 'subscene'
    _target = 'subscene'
    _category = 'subtitle'
    _remote_url = 'https://subscene.com/subtitles/searchbytitle?query={query}'
    _accepted_result_pattern = re.compile(r'(https?://(www\.)?subscene\.com/subtitles/[^/]+)$',
                                          re.IGNORECASE)
    BASE_URL = 'https://subscene.com'

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param BeautifulSoup response: html response.

        :keyword int year: movie year. if not provided, the
                           subscene url will not be matched.

        :rtype: list[str]
        """

        urls = []
        year = options.get('year')
        if year is None:
            return urls

        result_container = response.find('div', class_='search-result')
        if result_container is None:
            return urls

        results = result_container.find_all('a', href=True)
        for item in results:
            if not self._is_year_match(item.get_text(strip=True), year):
                continue

            full_url = '{base}{url}'.format(base=self.BASE_URL, url=item.get('href'))
            urls.append(full_url)

        return list(set(urls))

    def _is_year_match(self, name, year):
        """
        gets a value indicating that the provided name contains the given year.

        :param str name: movie name.
        :param int year: movie year.

        :rtype: bool
        """

        if year is None:
            return False

        return '({year})'.format(year=year) in name
