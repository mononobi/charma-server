# -*- coding: utf-8 -*-
"""
updater handlers content rate module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class ContentRateUpdater(UpdaterBase):
    """
    content rate updater class.
    """

    _category = UpdaterCategoryEnum.CONTENT_RATE

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb content rate.
        """

        content_rate = None
        content_rate_container = content.find('div', class_='title_wrapper')
        if content_rate_container is not None:
            content_rate_tag = content_rate_container.find('div', class_='subtext')
            content_rate = self._get_text(content_rate_tag, **options)

        return content_rate
