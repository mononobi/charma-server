# -*- coding: utf-8 -*-
"""
search providers oscobo module.
"""

import re

from imovie.search.providers.base import SearchProviderBase


class OscoboSearchProviderBase(SearchProviderBase):
    """
    oscobo search provider base class.
    """

    SEARCH_URL = 'https://www.oscobo.com/search.php?q={query}'
    ACCEPTED_RESULT_PATTERN = re.compile(r'^.+\.imdb\.com/title/.+$', re.IGNORECASE)

    def find(self, text, limit, **options):
        """
        gets the founded url for given text.

        it may return None if no url matched the `accepted_result_pattern`.

        :param str text: text to be searched.
        :param int limit: max number of urls to be tried before giving
                          up the search. defaults to 5 if not provided.
                          it could not be more than 10.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        query = self.get_search_query(text)

    def get_search_query(self, text):
        """
        gets the search query for given text.

        :param str text: text to be searched.

        :rtype: str
        """

        return self.search_url.format(query=text)

    @property
    def search_url(self):
        """
        gets the search url of this search provider.

        :rtype: str
        """

        return self.SEARCH_URL

    @property
    def accepted_result_pattern(self):
        """
        gets the accepted result pattern of this search provider.

        :rtype: re.Pattern
        """

        return self.ACCEPTED_RESULT_PATTERN
