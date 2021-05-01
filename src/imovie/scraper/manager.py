# -*- coding: utf-8 -*-
"""
scraper manager module.
"""

import requests

from bs4 import BeautifulSoup

import pyrin.configuration.services as config_services

from pyrin.core.structs import Manager

from imovie.scraper import ScraperPackage


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
        gets the result of given url and returns a `BeautifulSoup` object.

        :param str url: url to be fetched.

        :keyword bool add_user_agent: add user agent into request headers.
                                      defaults to True if not provided.

        :keyword dict headers: headers to be sent with request.

        :rtype: BeautifulSoup
        """

        headers = options.get('headers') or {}
        add_user_agent = options.get('add_user_agent', True)
        if add_user_agent is True:
            headers['User-Agent'] = self._user_agent

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, self._parser)
