# -*- coding: utf-8 -*-
"""
updater handlers title module.
"""

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBTitleUpdater(UpdaterBase):
    """
    imdb title updater class.
    """

    _name = 'imdb_title'
    _category = 'title'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb title.
        """

        title = None
        title_container = content.find('div', class_='title_wrapper')
        if title_container is not None:
            title_tag = content.find('h1', class_=True)
            title = self._get_text(title_tag, **options)

        return title
