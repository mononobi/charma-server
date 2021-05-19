# -*- coding: utf-8 -*-
"""
updater processors base module.
"""

from imovie.updater.interface import AbstractProcessor
from imovie.updater.exceptions import IMDBPageIsNotProvidedError


class ProcessorBase(AbstractProcessor):
    """
    processor base class.
    """

    # the category of this processor.
    # it is actually the relevant entity's column name.
    _category = None

    def _get_imdb_page(self, **options):
        """
        gets imdb page from given options.

        it raises an error if imdb page is not present in options.

        :keyword str imdb_page: movie imdb page.

        :raises IMDBPageIsNotProvidedError: imdb page is not provided error.

        :rtype: str
        """

        imdb_page = options.get('imdb_page')
        if imdb_page in (None, ''):
            raise IMDBPageIsNotProvidedError('IMDb page is not provided in options.')

        return imdb_page

    @property
    def name(self):
        """
        gets the name of this processor.

        :rtype: str
        """

        return self.get_name()

    @property
    def category(self):
        """
        gets the category of this processor.

        :rtype: str
        """

        return self._category
