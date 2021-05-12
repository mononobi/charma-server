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
    def fetch(self, url, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.

        :keyword bs4.BeautifulSoup content: the html content of input url.

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


class ProcessorSingletonMeta(MultiSingletonMeta):
    """
    processor singleton meta class.
    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractProcessor(CoreObject, metaclass=ProcessorSingletonMeta):
    """
    abstract processor class.
    """

    @abstractmethod
    def process(self, movie_id, data, **options):
        """
        processes given update data and returns the processed data.

        it may return None if processed data should not be used.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param object data: update data to be processed.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: processed data
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def name(self):
        """
        gets the name of this processor.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def category(self):
        """
        gets the category of this processor.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()
