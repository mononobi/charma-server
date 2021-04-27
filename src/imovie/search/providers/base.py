# -*- coding: utf-8 -*-
"""
search providers base module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

from imovie.search.interface import AbstractSearchProvider


class SearchProviderBase(AbstractSearchProvider):
    """
    search provider base class.
    """

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
    @abstractmethod
    def search_url(self):
        """
        gets the search url of this search provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def accepted_result_pattern(self):
        """
        gets the accepted result pattern of this search provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: re.Pattern
        """

        raise CoreNotImplementedError()
