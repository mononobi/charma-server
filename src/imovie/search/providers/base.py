# -*- coding: utf-8 -*-
"""
search providers base module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

import imovie.scraper.services as scraper_services

from imovie.search.interface import AbstractSearchProvider


class SearchProviderBase(AbstractSearchProvider):
    """
    search provider base class.
    """

    # the name of this search provider.
    _name = None

    # the target of this search provider.
    _target = None

    # the category of this search provider.
    _category = None

    # the accepted result url pattern for this provider.
    # it must consider the result in group 1 (not 0).
    # it must be a compiled pattern.
    _accepted_result_pattern = None

    # the remote url of this provider to make requests to it.
    # it must have '{query}' and '{target}' place-holders in it.
    _remote_url = None

    def __prepare_url(self, url):
        """
        prepares given matched url to be returned by this provider.

        :param str url: url to be prepared.

        :rtype: str
        """

        if url is None:
            return url

        return self._prepare_url(url)

    def __extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param bs4.BeautifulSoup response: html response.

        :rtype: list[str]
        """

        result = self._extract_urls(response, **options)
        if result is None or len(result) <= 0:
            return None

        return result

    def _fetch(self, url, **options):
        """
        fetches the result of given url.

        :param str url: url to be fetched.

        :rtype: bs4.BeautifulSoup
        """

        return scraper_services.get(url, **options)

    def _prepare_url(self, url):
        """
        prepares given matched url to be returned by this provider.

        subclasses could override this if needed.

        :param str url: url to be prepared.

        :rtype: str
        """

        return url

    def search(self, text, **options):
        """
        searches given text and returns a url.

        it may return None if nothing found.

        :param str text: text to be searched.

        :keyword int limit: max number of urls to be tried before giving
                            up the search. defaults to 10 if not provided.
                            it could not be more than 20.

        :rtype: str
        """

        limit = options.get('limit', 10)
        if limit <= 0:
            limit = 1

        limit = min(limit, 20)
        query = self.get_search_query(text)
        response = self._fetch(query, **options)
        urls = self.__extract_urls(response, **options)
        if urls is None:
            return None

        found_url = None
        count = 0
        for item in urls:
            count += 1
            matched = self.accepted_result_pattern.match(item)
            if matched:
                found_url = matched.group(1)
                break

            if count >= limit:
                break

        return self.__prepare_url(found_url)

    def get_search_query(self, text):
        """
        gets the search query for given text.

        :param str text: text to be searched.

        :rtype: str
        """

        return self.remote_url.format(query=text, target=self.target)

    @property
    def name(self):
        """
        gets the name of this search provider.

        the name will be constructed in the form of `name`.`target`.
        for example `oscobo.imdb`.

        :rtype: str
        """

        return '{name}.{target}'.format(name=self._name, target=self.target)

    @property
    def target(self):
        """
        gets the target of this search provider.

        :rtype: str
        """

        return self._target

    @property
    def category(self):
        """
        gets the category of this provider.

        :rtype: str
        """

        return self._category

    @property
    def accepted_result_pattern(self):
        """
        gets the accepted result pattern of this search provider.

        :rtype: re.Pattern
        """

        return self._accepted_result_pattern

    @property
    def remote_url(self):
        """
        gets the remote url of this search provider.

        :rtype: str
        """

        return self._remote_url

    @abstractmethod
    def _extract_urls(self, response, **options):
        """
        extracts available urls from given response.

        it may return None if nothing found.

        :param bs4.BeautifulSoup response: html response.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: list[str]
        """

        raise CoreNotImplementedError
