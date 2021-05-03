# -*- coding: utf-8 -*-
"""
updater handlers base module.
"""

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

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
        :param BeautifulSoup content: the html content of input url.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: update data
        """

        raise CoreNotImplementedError()

    def fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param BeautifulSoup content: the html content of input url.

        :returns: update data
        """

        data = self._fetch(url, content, **options)
        if data is None:
            if self._next_handler is not None:
                return self._next_handler.fetch(url, content, **options)

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
