# -*- coding: utf-8 -*-
"""
search providers oscobo module.
"""

from charma.search.decorators import search_provider
from charma.search.providers.base import SearchProviderBase
from charma.search.providers.mixin import IMDBMovieMixin


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

        :param bs4.BeautifulSoup response: html response.

        :rtype: list[str]
        """

        urls = []
        result_container = response.find('div', id='results-list')
        if result_container is None:
            return urls

        results = result_container.find_all('div', class_='line cite')
        for item in results:
            urls.append(item.get_text(strip=True))

        return urls


@search_provider()
class OscoboIMDBProvider(IMDBMovieMixin, OscoboBase):
    """
    oscobo imdb provider class.
    """
    pass
