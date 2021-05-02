# -*- coding: utf-8 -*-
"""
search providers bing module.
"""

from imovie.search.decorators import search_provider
from imovie.search.providers.base import SearchProviderBase
from imovie.search.providers.mixins import IMDBMovieMixin


class BingBase(SearchProviderBase):
    """
    bing base class.
    """

    _name = 'bing'
    _remote_url = 'https://www.bing.com/search?q={query} {target}'

    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param BeautifulSoup response: html response.

        :rtype: list[str]
        """

        urls = []
        result_container = response.find('ol', id='b_results')
        if result_container is None:
            return urls

        results = result_container.find_all('cite')
        for item in results:
            urls.append(item.get_text(strip=True))

        return urls


@search_provider()
class BingIMDBProvider(IMDBMovieMixin, BingBase):
    """
    bing imdb provider class.
    """
    pass
