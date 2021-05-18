# -*- coding: utf-8 -*-
"""
updater handlers country module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class CountryUpdater(UpdaterBase):
    """
    country updater class.
    """

    _category = UpdaterCategoryEnum.COUNTRY

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of imdb countries.
        :rtype: list[str]
        """

        countries = []
        country_section = content.find('div', class_='article', id='titleDetails')
        if country_section is not None:
            potential_country = country_section.find_all('h4', class_='inline')
            for item in potential_country:
                text = self._get_text(item)
                if text is not None and 'country' in text.lower() and item.parent is not None:
                    results = item.parent.find_all('a', href=True)
                    for node in results:
                        name = node.get_text(strip=True)
                        if len(name) > 0:
                            countries.append(name)

                    break

        return countries or None
