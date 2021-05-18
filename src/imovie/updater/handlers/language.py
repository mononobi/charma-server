# -*- coding: utf-8 -*-
"""
updater handlers language module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class LanguageUpdater(UpdaterBase):
    """
    language updater class.
    """

    _category = UpdaterCategoryEnum.LANGUAGE

    def _fetch(self, content, **options):
        """
        fetches data from given url.

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
