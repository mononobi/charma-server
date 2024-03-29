# -*- coding: utf-8 -*-
"""
updater handlers person module.
"""

import re

from abc import abstractmethod

from pyrin.logging.contexts import suppress
from pyrin.core.exceptions import CoreNotImplementedError

import charma.scraper.services as scraper_services

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase
from charma.updater.handlers.mixin import ImageFetcherMixin


class PersonUpdaterBase(UpdaterBase, ImageFetcherMixin):
    """
    person updater base class.
    """

    BASE_URL = 'https://www.imdb.com'
    PERSON_URL_PATTERN = re.compile(r'^(/name/nm[\d]+)[.]*', flags=re.IGNORECASE)
    IMAGE_WIDTH = 256
    IMAGE_HEIGHT = 380

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: list of persons.
        :rtype: list[dict]
        """

        credits_content = options.pop('credits', None)
        if credits_content is None:
            return

        return self._fetch_data(content, credits_content, **options)

    def _get_person_url(self, url):
        """
        gets the person imdb page url from given url.

        it returns None if it could not get the imdb page.

        :param str url: url to get person page url from it.

        :rtype: str
        """

        if url is None:
            return None

        matched = re.match(self.PERSON_URL_PATTERN, url)
        if matched:
            sub_url = matched.group(1)
            return '{base}{sub_url}'.format(base=self.BASE_URL, sub_url=sub_url)

        return None

    @abstractmethod
    def _fetch_data(self, content, credits_content, **options):
        """
        fetches data from given content and credits content.

        :param bs4.BeautifulSoup content: the html content of imdb page.
        :param bs4.BeautifulSoup credits_content: the html content of credits page.

        :raises CoreNotImplementedError: core not implemented error.

        :returns: list of persons.
        :rtype: list[dict]
        """

        raise CoreNotImplementedError()


class PersonUpdater(PersonUpdaterBase):
    """
    person updater class.
    """

    def _get_fullname_and_imdb_page(self, tag, class_):
        """
        gets the fullname and imdb page of actor.

        it may return None for each value if it is not available.

        :param bs4.Tag tag: tag to fetch fullname and imdb page from.
        :param bool | str class_: the class attribute of corresponding `td` tag.

        :returns: tuple[str fullname, str imdb_page]
        :rtype: tuple[str, str]
        """

        actor_tag = tag.find('td', class_=class_)
        if actor_tag is not None:
            actor_info = actor_tag.find('a', href=True)
            if actor_info is not None:
                name = actor_info.get_text(separator=' ', strip=True) or None
                url = self._get_person_url(actor_info.get('href')) or None
                return name, url

        return None, None


class ActorUpdaterBase(PersonUpdaterBase):
    """
    actor updater base class.
    """

    _category = UpdaterCategoryEnum.ACTORS

    def _get_stars(self, content):
        """
        gets imdb page of all star actors.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :rtype: list[str]
        """

        stars = self._get_stars_v1(content)
        if len(stars) <= 0:
            stars = self._get_stars_v2(content)

        return stars

    def _get_stars_v1(self, content):
        """
        gets imdb page of all star actors.

        this method works with old imdb page.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :rtype: list[str]
        """

        possible_star_containers = content.find_all('div', class_='credit_summary_item')
        stars = []
        for item in possible_star_containers:
            section_tag = item.find('h4', class_='inline')
            text = self._get_text(section_tag)
            if text is not None and 'stars' in text.lower():
                results = item.find_all('a', href=True)
                for node in results:
                    url = self._get_person_url(node.get('href'))
                    if url is not None:
                        stars.append(url)

                break

        return stars

    def _get_stars_v2(self, content):
        """
        gets imdb page of all star actors.

        this method works with new imdb page.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :rtype: list[str]
        """

        star_container = content.find('div', {'data-testid': 'title-pc-wide-screen'})
        stars = []
        if star_container is not None:
            possible_star_containers = star_container.find_all(
                'li', {'data-testid': 'title-pc-principal-credit'})
            reversed_containers = reversed(possible_star_containers)
            for item in reversed_containers:
                name_tag = item.find('a', href=True, recursive=False)
                if name_tag is not None:
                    name = name_tag.get_text(strip=True)
                    if 'stars' in name.lower():
                        stars_list = item.find('ul', class_=True)
                        if stars_list is not None:
                            results = stars_list.find_all('a', href=True)
                            for single_star in results:
                                url = self._get_person_url(single_star.get('href'))
                                if url is not None:
                                    stars.append(url)

                        break

        return stars


@updater()
class ActorUpdater(ActorUpdaterBase, PersonUpdater):
    """
    actor updater class.
    """

    def _get_character(self, tag):
        """
        gets the character of actor.

        it may return None if character is not available.

        :param bs4.Tag tag: tag to fetch character from.

        :rtype: str
        """

        character_tag = tag.find('td', class_='character')
        if character_tag is not None:
            return character_tag.get_text(separator=' ', strip=True) or None

        return None

    def _get_photo_url(self, tag):
        """
        gets photo url of actor.

        it returns None if it fails to fetch photo url.

        :param bs4.Tag tag: tag to fetch photo url from.

        :rtype: str
        """

        photo_container = tag.find('td', class_='primary_photo')
        if photo_container is not None:
            photo_tag = photo_container.find('img', loadlate=True)
            if photo_tag is not None:
                return self.get_resized_image_url(photo_tag.get('loadlate'),
                                                  self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        return None

    def _fetch_data(self, content, credits_content, **options):
        """
        fetches data from given content and credits content.

        :param bs4.BeautifulSoup content: the html content of imdb page.
        :param bs4.BeautifulSoup credits_content: the html content of credits page.

        :returns: list[dict(str fullname,
                            str imdb_page,
                            str character,
                            str photo_name,
                            bool is_star)].
        :rtype: list[dict]
        """

        cast_list_container = credits_content.find('table', class_='cast_list')
        stars = self._get_stars(content)
        actors = []
        if cast_list_container is not None:
            odd_rows = cast_list_container.find_all('tr', class_='odd')
            even_rows = cast_list_container.find_all('tr', class_='even')
            all_rows = []
            all_rows.extend(odd_rows)
            all_rows.extend(even_rows)
            for item in all_rows:
                fullname, imdb_page = self._get_fullname_and_imdb_page(item, class_=False)
                character = self._get_character(item)
                photo_name = self._get_photo_url(item)
                single_actor = dict(fullname=fullname, imdb_page=imdb_page,
                                    character=character, photo_name=photo_name,
                                    is_star=imdb_page in stars)

                actors.append(single_actor)

        return actors or None


class DirectorUpdaterBase(PersonUpdaterBase):
    """
    director updater base class.
    """

    _category = UpdaterCategoryEnum.DIRECTORS


@updater()
class DirectorUpdater(DirectorUpdaterBase, PersonUpdater):
    """
    director updater class.
    """

    def _get_photo_url(self, imdb_page):
        """
        gets photo url of director.

        it returns None if it fails to fetch photo url.

        :param str imdb_page: imdb page url of director.

        :rtype: str
        """

        if imdb_page is None:
            return None

        with suppress():
            content = scraper_services.get_soup(imdb_page)
            poster_tag = content.find('img', id='name-poster', src=True)
            if poster_tag is not None:
                return self.get_resized_image_url(poster_tag.get('src'),
                                                  self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        return None

    def _fetch_data(self, content, credits_content, **options):
        """
        fetches data from given content and credits content.

        :param bs4.BeautifulSoup content: the html content of imdb page.
        :param bs4.BeautifulSoup credits_content: the html content of credits page.

        :returns: list[dict(str fullname,
                            str imdb_page,
                            str photo_name,
                            bool is_main)].
        :rtype: list[dict]
        """

        directors = []
        directors_title = credits_content.find('h4', attrs=dict(name='director'), id='director')
        if directors_title is not None:
            director_list_container = directors_title.find_next(
                'table', class_='simpleTable simpleCreditsTable')
            if director_list_container is not None:
                directors_list = director_list_container.find_all('tr')
                for index, item in enumerate(directors_list):
                    fullname, imdb_page = self._get_fullname_and_imdb_page(item, class_='name')
                    photo_name = self._get_photo_url(imdb_page)
                    single_director = dict(fullname=fullname, imdb_page=imdb_page,
                                           photo_name=photo_name, is_main=index == 0)

                    directors.append(single_director)

        return directors or None
