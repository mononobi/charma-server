# -*- coding: utf-8 -*-
"""
updater handlers original title module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class OriginalTitleUpdater(UpdaterBase):
    """
    original title updater class.
    """

    _category = UpdaterCategoryEnum.ORIGINAL_TITLE

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb original title.
        """

        original_title_tag = content.find('div', class_='originalTitle')
        original_title = self._get_text(original_title_tag, **options)

        return original_title
