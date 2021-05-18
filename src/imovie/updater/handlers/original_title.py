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

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb original title.
        """

        original_title_tag = content.find('div', class_='originalTitle')
        original_title = self._get_text(original_title_tag, **options)

        return original_title
