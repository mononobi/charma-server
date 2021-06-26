# -*- coding: utf-8 -*-
"""
persons handler module.
"""

from abc import abstractmethod
from threading import Lock

from pyrin.core.structs import CoreObject, MultiSingletonMeta
from pyrin.core.exceptions import CoreNotImplementedError


class PersonHandlerSingletonMeta(MultiSingletonMeta):
    """
    person handler singleton meta class.

    this is a thread-safe implementation of singleton.
    """

    _instances = dict()
    _lock = Lock()


class AbstractPersonHandler(CoreObject, metaclass=PersonHandlerSingletonMeta):
    """
    abstract person handler class.
    """

    # handler name. it must be set in subclasses.
    name = None

    @abstractmethod
    def create(self, id, **options):
        """
        creates a person with given inputs.

        :param uuid.UUID id: person id.

        :raises CoreNotImplementedError: core not implemented error.
        """

        raise CoreNotImplementedError()
