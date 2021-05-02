# -*- coding: utf-8 -*-
"""
search providers oscobo module.
"""

from imovie.search.decorators import search_provider
from imovie.search.providers.base import SearchProviderBase
from imovie.search.providers.mixins import IMDBMovieMixin


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
