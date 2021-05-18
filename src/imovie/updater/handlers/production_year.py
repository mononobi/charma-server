# -*- coding: utf-8 -*-
"""
updater handlers production year module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class ProductionYearUpdater(UpdaterBase):
    """
    production year updater class.
    """

    _category = UpdaterCategoryEnum.PRODUCTION_YEAR

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
