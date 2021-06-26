# -*- coding: utf-8 -*-
"""
scraper services module.
"""

from pyrin.application.services import get_component

from charma.scraper import ScraperPackage


def get(url, **options):
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

    return get_component(ScraperPackage.COMPONENT_NAME).get(url, **options)


def get_soup(url, **options):
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

    return get_component(ScraperPackage.COMPONENT_NAME).get_soup(url, **options)
