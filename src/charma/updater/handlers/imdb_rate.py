# -*- coding: utf-8 -*-
"""
updater handlers imdb rate module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class IMDBRateUpdaterBase(UpdaterBase):
    """
    imdb rate updater base class.
    """

    _category = UpdaterCategoryEnum.IMDB_RATE


@updater()
class IMDBRateUpdater(IMDBRateUpdaterBase):
    """
    imdb rate updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb rate.
        :rtype: float
        """

        rate = None
        rate_tag = content.find('span', itemprop='ratingValue')
        if rate_tag is not None:
            result = rate_tag.get_text(strip=True)
            if len(result) > 0:
                rate = float(result)

        return rate


@updater()
class IMDBRateUpdaterV2(IMDBRateUpdaterBase):
    """
    imdb rate updater v2 class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb rate.
        :rtype: float
        """

        rate = None
        rate_container = content.find(
            'div', {'data-testid': 'hero-title-block__aggregate-rating__score'})

        if rate_container is not None:
            rate_tag = rate_container.find('span', class_=True)
            if rate_tag is not None:
                result = rate_tag.get_text(strip=True)
                if len(result) > 0:
                    rate = float(result)

        return rate
