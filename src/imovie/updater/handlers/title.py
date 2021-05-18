# -*- coding: utf-8 -*-
"""
updater handlers title module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class TitleUpdater(UpdaterBase):
    """
    title updater class.
    """

    _category = UpdaterCategoryEnum.TITLE

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb title.
        :rtype: str
        """

        title = None
        title_container = content.find('div', class_='title_wrapper')
        if title_container is not None:
            title_tag = content.find('h1', class_=True)
            title = self._get_text(title_tag, **options)

        return title
