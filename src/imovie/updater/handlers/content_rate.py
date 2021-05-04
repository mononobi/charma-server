# -*- coding: utf-8 -*-
"""
updater handlers content rate module.
"""

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class ContentRateUpdater(UpdaterBase):
    """
    content rate updater class.
    """

    _name = 'content_rate'
    _category = 'content_rate'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: update data
        """

        content_rate = None
        content_rate_container = content.find('div', class_='title_wrapper')
        if content_rate_container is not None:
            content_rate_tag = content_rate_container.find('div', class_='subtext')
            if content_rate_tag is not None:
                content_rate = content_rate_tag.get_text(strip=True)

        return content_rate


# import imovie.updater.services as se
# d = se.fetch('https://www.imdb.com/title/tt10272386/', 'content_rate')
# f = 0