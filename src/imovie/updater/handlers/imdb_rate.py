# -*- coding: utf-8 -*-
"""
updater handlers imdb rate module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBRateUpdater(UpdaterBase):
    """
    imdb rate updater class.
    """

    _category = UpdaterCategoryEnum.IMDB_RATE

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb rate.
        """

        rate = None
        rate_tag = content.find('span', itemprop='ratingValue')
        if rate_tag is not None:
            result = rate_tag.get_text(strip=True)
            if len(result) > 0:
                rate = float(result)

        return rate
