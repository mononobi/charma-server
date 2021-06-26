# -*- coding: utf-8 -*-
"""
updater handlers language module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class LanguageUpdaterBase(UpdaterBase):
    """
    language updater base class.
    """

    _category = UpdaterCategoryEnum.LANGUAGE


@updater()
class LanguageUpdater(LanguageUpdaterBase):
    """
    language updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of imdb languages.
        :rtype: list[str]
        """

        languages = []
        language_section = content.find('div', class_='article', id='titleDetails')
        if language_section is not None:
            potential_language = language_section.find_all('h4', class_='inline')
            for item in potential_language:
                text = self._get_text(item)
                if text is not None and 'language' in text.lower() and item.parent is not None:
                    results = item.parent.find_all('a', href=True)
                    for node in results:
                        name = node.get_text(strip=True)
                        if len(name) > 0:
                            languages.append(name)

                    break

        return languages or None


@updater()
class LanguageUpdaterV2(LanguageUpdaterBase):
    """
    language updater v2 class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of imdb languages.
        :rtype: list[str]
        """

        languages = []
        language_section = content.find('li', {'data-testid': 'title-details-languages'})
        if language_section is not None:
            language_list = language_section.find('ul', class_=True)
            if language_list is not None:
                language_tags = language_list.find_all('a', href=True)
                for item in language_tags:
                    name = item.get_text(strip=True)
                    if len(name) > 0:
                        languages.append(name)

        return languages or None
