# -*- coding: utf-8 -*-
"""
updater handlers rate module.
"""

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBRateUpdater(UpdaterBase):
    """
    imdb rate updater class.
    """

    _name = 'imdb_rate'
    _category = 'rate'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: update data
        """

        rate = None
        rate_tag = content.find('span', itemprop='ratingValue')
        if rate_tag is not None:
            rate = rate_tag.get_text(strip=True)
            rate = float(rate)

        return rate
