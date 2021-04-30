# -*- coding: utf-8 -*-
"""
search interface module.
"""

from threading import Lock
from abc import abstractmethod

from pyrin.core.structs import CoreObject, MultiSingletonMeta
from pyrin.core.exceptions import CoreNotImplementedError


class SearchProviderSingletonMeta(MultiSingletonMeta):
    """
    search provider singleton meta class.
    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractSearchProvider(CoreObject, metaclass=SearchProviderSingletonMeta):
    """
    abstract search provider class.
    """

    @abstractmethod
    def search(self, text, **options):
        """
        searches given text and returns a url.

        it may return None if nothing found.

        :param str text: text to be searched.

        :keyword int limit: max number of urls to be tried before giving
                            up the search. defaults to 5 if not provided.
                            it could not be more than 10.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def name(self):
        """
        gets the name of this search provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    @property
    @abstractmethod
    def category(self):
        """
        gets the category of this provider.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()
