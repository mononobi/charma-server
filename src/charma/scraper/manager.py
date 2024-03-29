# -*- coding: utf-8 -*-
"""
scraper manager module.
"""

import requests

from bs4 import BeautifulSoup

import pyrin.configuration.services as config_services

from pyrin.core.structs import Manager
from pyrin.processor.request.enumerations import RequestHeaderEnum

from charma.scraper import ScraperPackage


class ScraperManager(Manager):
    """
    scraper manager class.
    """

    package_class = ScraperPackage

    def __init__(self):
        """
        initializes an instance of ScraperManager.
        """

        super().__init__()

        self._user_agent = config_services.get('scraper', 'general', 'user_agent')
        self._parser = config_services.get('scraper', 'general', 'parser')

    def get(self, url, **options):
        """
        gets the result of given url and returns a `Response` object.

        :param str url: url to be fetched.

        :keyword bool add_user_agent: add user agent into request headers.
                                      defaults to True if not provided.

        :keyword bool allow_redirects: allow redirects.
                                       defaults to True if not provided.

        :keyword dict headers: headers to be sent with request.

        :rtype: requests.Response
        """

        headers = options.get('headers') or {}
        options.setdefault('allow_redirects', True)
        add_user_agent = options.pop('add_user_agent', True)
        if add_user_agent is True:
            headers[RequestHeaderEnum.USER_AGENT] = self._user_agent

        # we have to set 'Accept-Language' header to 'en-US'
        # to get consistent results for any movie on any client.
        headers[RequestHeaderEnum.ACCEPT_LANGUAGE] = 'en-US'
        options.update(headers=headers)
        response = requests.get(url, **options)
        response.raise_for_status()
        return response

    def get_soup(self, url, **options):
        """
        gets the result of given url and returns a `BeautifulSoup` object.

        :param str url: url to be fetched.

        :keyword bool add_user_agent: add user agent into request headers.
                                      defaults to True if not provided.

        :keyword bool allow_redirects: allow redirects.
                                       defaults to True if not provided.

        :keyword dict headers: headers to be sent with request.

        :rtype: bs4.BeautifulSoup
        """

        response = self.get(url, **options)
        return BeautifulSoup(response.text, self._parser)
