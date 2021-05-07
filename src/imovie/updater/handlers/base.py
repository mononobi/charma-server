# -*- coding: utf-8 -*-
"""
updater handlers base module.
"""

from abc import abstractmethod

from bs4 import NavigableString

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.exceptions import CoreNotImplementedError

import imovie.scraper.services as scraper_services

from imovie.updater.interface import AbstractUpdater
from imovie.updater.exceptions import InvalidUpdaterTypeError


class UpdaterBase(AbstractUpdater):
    """
    updater base class.
    """

    # the name of this updater.
    _name = None

    # the category of this updater.
    _category = None

    def __init__(self, **options):
        """
        initializes an instance of UpdaterBase.
        """

        super().__init__()
        self._next_handler = None

    @abstractmethod
    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: update data
        """

        raise CoreNotImplementedError()

    def _update_url(self, url):
        """
        updates given url and returns the new url.

        this method is intended to be overridden in subclasses.

        :param str url: url to be updated.

        :rtype: str
        """

        return url

    def _get_text(self, tag, **options):
        """
        gets the string of `next` attribute of given tag if available.

        otherwise returns None.

        :param bs4.element.Tag tag: a tag object.

        :rtype: str
        """

        text = None
        if tag is not None and isinstance(tag.next, NavigableString):
            result = normalizer_services.filter(str(tag.next), filters=['\n'])
            if len(result) > 0:
                text = result

        return text

    def fetch(self, url, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.

        :keyword bs4.BeautifulSoup content: the html content of input url.

        :returns: update data
        """

        new_url = self._update_url(url)
        content = options.get('content')
        if content is None or url != new_url:
            content = scraper_services.get(url, **options)

        options.update(content=content)
        data = self._fetch(new_url, content)
        if data is None:
            if self._next_handler is not None:
                return self._next_handler.fetch(new_url, **options)

        return data

    def set_next(self, updater):
        """
        sets the next updater handler and returns it.

        :param UpdaterBase updater: updater instance to
                                    be set as next handler.

        :raises InvalidUpdaterTypeError: invalid updater error.

        :rtype: UpdaterBase
        """

        if updater is not None and not isinstance(updater, UpdaterBase):
            raise InvalidUpdaterTypeError('Input parameter [{instance}] is not '
                                          'an instance of [{base}].'
                                          .format(instance=updater,
                                                  base=UpdaterBase))

        self._next_handler = updater
        return updater

    @property
    def name(self):
        """
        gets the name of this updater.

        :rtype: str
        """

        return self._name

    @property
    def category(self):
        """
        gets the category of this updater.

        :rtype: str
        """

        return self._category
