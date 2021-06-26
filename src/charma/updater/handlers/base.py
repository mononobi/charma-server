# -*- coding: utf-8 -*-
"""
updater handlers base module.
"""

from abc import abstractmethod

from bs4 import NavigableString

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.exceptions import CoreNotImplementedError

from charma.updater.interface import AbstractUpdater
from charma.updater.exceptions import InvalidUpdaterTypeError


class UpdaterBase(AbstractUpdater):
    """
    updater base class.
    """

    # the category of this updater.
    # it is actually the relevant entity's column name.
    _category = None

    def __init__(self, **options):
        """
        initializes an instance of UpdaterBase.
        """

        super().__init__()
        self._next_handler = None

    @abstractmethod
    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: update data
        """

        raise CoreNotImplementedError()

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

    def fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: update data
        """

        data = self._fetch(content, **options)
        if data is None:
            if self._next_handler is not None:
                return self._next_handler.fetch(content, **options)

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

        return self.get_name()

    @property
    def category(self):
        """
        gets the category of this updater.

        :rtype: str
        """

        return self._category
