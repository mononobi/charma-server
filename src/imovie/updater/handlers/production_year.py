# -*- coding: utf-8 -*-
"""
updater handlers production year module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBProductionYearUpdater(UpdaterBase):
    """
    imdb production year updater class.
    """

    _name = 'imdb_production_year'
    _category = 'production_year'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb production year.
        """

        production_year = None
        production_year_tag = content.find('span', id='titleYear')
        if production_year_tag is not None:
            result = production_year_tag.get_text(strip=True)
            result = normalizer_services.filter(result, filters=['\n', r'\(', r'\)'])
            if result.isdigit():
                production_year = int(result)

        return production_year
