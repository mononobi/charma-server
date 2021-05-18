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

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb rate.
        """

        rate = None
        rate_tag = content.find('span', itemprop='ratingValue')
        if rate_tag is not None:
            result = rate_tag.get_text(strip=True)
            if len(result) > 0:
                rate = float(result)

        return rate
