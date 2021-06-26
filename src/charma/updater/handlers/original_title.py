# -*- coding: utf-8 -*-
"""
updater handlers original title module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class OriginalTitleUpdaterBase(UpdaterBase):
    """
    original title updater base class.
    """

    _category = UpdaterCategoryEnum.ORIGINAL_TITLE


@updater()
class OriginalTitleUpdater(OriginalTitleUpdaterBase):
    """
    original title updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb original title.
        :rtype: str
        """

        original_title_tag = content.find('div', class_='originalTitle')
        original_title = self._get_text(original_title_tag, **options)

        return original_title


@updater()
class OriginalTitleUpdaterV2(OriginalTitleUpdaterBase):
    """
    original title updater v2 class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb original title.
        :rtype: str
        """

        original_title = None
        original_title_tag = content.find('div',
                                          {'data-testid': 'hero-title-block__original-title'})
        if original_title_tag is not None:
            raw_original_title = original_title_tag.get_text(strip=True)
            raw_original_title = normalizer_services.filter(raw_original_title,
                                                            filters=['original title:'])
            if len(raw_original_title) > 0:
                original_title = raw_original_title

        return original_title
