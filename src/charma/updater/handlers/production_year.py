# -*- coding: utf-8 -*-
"""
updater handlers production year module.
"""

import re

import pyrin.utilities.string.normalizer.services as normalizer_services

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class ProductionYearUpdaterBase(UpdaterBase):
    """
    production year updater base class.
    """

    _category = UpdaterCategoryEnum.PRODUCTION_YEAR


@updater()
class ProductionYearUpdater(ProductionYearUpdaterBase):
    """
    production year updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb production year.
        :rtype: int
        """

        production_year = None
        production_year_tag = content.find('span', id='titleYear')
        if production_year_tag is not None:
            result = production_year_tag.get_text(strip=True)
            result = normalizer_services.filter(result, filters=['\n', r'\(', r'\)'])
            if result.isdigit():
                production_year = int(result)

        return production_year


@updater()
class ProductionYearUpdaterV2(ProductionYearUpdaterBase):
    """
    production year updater v2 class.
    """

    RELEASE_INFO_URL_REGEX = re.compile(r'^.+/releaseinfo.*', re.IGNORECASE)

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb production year.
        :rtype: int
        """

        production_year = None
        metadata_list = content.find('ul', {'data-testid': 'hero-title-block__metadata'})
        if metadata_list is not None:
            production_year_tag = metadata_list.find('a', href=self.RELEASE_INFO_URL_REGEX)
            if production_year_tag is not None:
                result = production_year_tag.get_text(strip=True)
                if result.isdigit():
                    production_year = int(result)

        return production_year
