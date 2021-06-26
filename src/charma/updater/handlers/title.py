# -*- coding: utf-8 -*-
"""
updater handlers title module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class TitleUpdaterBase(UpdaterBase):
    """
    title updater base class.
    """

    _category = UpdaterCategoryEnum.TITLE


@updater()
class TitleUpdater(TitleUpdaterBase):
    """
    title updater class.
    """

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


@updater()
class TitleUpdaterV2(TitleUpdaterBase):
    """
    title updater v2 class.
    """

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
        title_tag = content.find('h1', {'data-testid': 'hero-title-block__title'})
        if title_tag is not None:
            title = title_tag.get_text(strip=True)

        return title or None
