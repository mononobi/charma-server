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
    def find(self, text, limit, **options):
        """
        gets the founded url for given text.

        it may return None if no url matched the `accepted_result_pattern`.

        :param str text: text to be searched.
        :param int limit: max number of urls to be tried before giving
                          up the search. defaults to 5 if not provided.

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
