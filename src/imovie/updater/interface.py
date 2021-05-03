# -*- coding: utf-8 -*-
"""
updater interface module.
"""

from threading import Lock
from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError
from pyrin.core.structs import MultiSingletonMeta, CoreObject


class UpdaterSingletonMeta(MultiSingletonMeta):
    """
    updater singleton meta class.
    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractUpdater(CoreObject, metaclass=UpdaterSingletonMeta):
    """
    abstract updater class.
    """

    @abstractmethod
    def fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param BeautifulSoup content: the html content of input url.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: update data
        """

        raise CoreNotImplementedError()

    @abstractmethod
    def set_next(self, updater):
        """
        sets the next updater handler and returns it.

        :param AbstractUpdater updater: updater instance to
                                        be set as next handler.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: AbstractUpdater
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def name(self):
        """
        gets the name of this updater.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def category(self):
        """
        gets the category of this updater.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()
