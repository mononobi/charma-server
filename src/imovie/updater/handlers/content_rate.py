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

    def _fetch(self, content, **options):
        """
        fetches data from given url.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb content rate.
        """

        content_rate = None
        content_rate_container = content.find('div', class_='title_wrapper')
        if content_rate_container is not None:
            content_rate_tag = content_rate_container.find('div', class_='subtext')
            content_rate = self._get_text(content_rate_tag, **options)

        return content_rate
