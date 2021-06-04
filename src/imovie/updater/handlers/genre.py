# -*- coding: utf-8 -*-
"""
updater handlers genre module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class GenreUpdater(UpdaterBase):
    """
    genre updater class.
    """

    _category = UpdaterCategoryEnum.GENRE

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of imdb genres.
        :rtype: list[str]
        """

        genres = []
        genre_section = content.find('div', class_='article', id='titleStoryLine')
        if genre_section is not None:
            potential_genre = genre_section.find_all('h4', class_='inline')
            for item in potential_genre:
                text = self._get_text(item)
                if text is not None and 'genre' in text.lower() and item.parent is not None:
                    results = item.parent.find_all('a', href=True)
                    for node in results:
                        name = node.get_text(strip=True)
                        if len(name) > 0:
                            genres.append(name)

                    break

        return genres or None


@updater()
class GenreUpdaterV2(UpdaterBase):
    """
    genre updater v2 class.
    """

    _category = UpdaterCategoryEnum.GENRE

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of imdb genres.
        :rtype: list[str]
        """

        genres = []
        genre_section = content.find('li', {'data-testid': 'storyline-genres'})
        if genre_section is not None:
            genre_list = genre_section.find('ul', class_=True)
            if genre_list is not None:
                genre_tags = genre_list.find_all('a', class_=True, href=True)
                for item in genre_tags:
                    name = item.get_text(strip=True)
                    if len(name) > 0:
                        genres.append(name)

        return genres or None
