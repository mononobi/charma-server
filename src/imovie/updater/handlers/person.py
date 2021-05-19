# -*- coding: utf-8 -*-
"""
updater handlers person module.
"""

import re

from abc import abstractmethod

from pyrin.core.exceptions import CoreNotImplementedError

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase
from imovie.updater.handlers.mixin import IMDBHighQualityImageFetcherMixin


class PersonUpdaterBase(UpdaterBase, IMDBHighQualityImageFetcherMixin):
    """
    person updater class.
    """

    BASE_URL = 'https://www.imdb.com'
    PERSON_URL_PATTERN = re.compile(r'^(/name/nm[\d]+)[.]*', flags=re.IGNORECASE)

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

        :param str url: url to get person page url from it.

        :rtype: str
        """

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


@updater()
class ActorUpdater(PersonUpdaterBase):
    """
    actor updater class.
    """

    _category = UpdaterCategoryEnum.ACTORS

    def _get_fullname_and_imdb_page(self, tag):
        """
        gets the fullname and imdb page of actor.

        it may return None for each value if it is not available.

        :param bs4.Tag tag: tag to fetch fullname and imdb page from.

        :returns: tuple[str fullname, str imdb_page]
        :rtype: tuple[str, str]
        """

        actor_tag = tag.find('td', class_=False)
        if actor_tag is not None:
            actor_info = actor_tag.find('a', href=True)
            if actor_info is not None:
                name = actor_info.get_text(separator=' ', strip=True) or None
                url = self._get_person_url(actor_info.get('href')) or None
                return name, url

        return None, None

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

    def _get_stars_imdb_page(self, content):
        """
        gets imdb pages of all star actors.

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

    def _get_photo_url(self, tag):
        """
        gets photo url of actor.

        :param bs4.Tag tag: tag to fetch photo url from.

        :rtype: str
        """

        photo_container = tag.find('td', class_='primary_photo')
        if photo_container is not None:
            photo_tag = photo_container.find('img', loadlate=True)
            if photo_tag is not None:
                result = photo_tag.get('loadlate')
                return self.get_high_quality_image_url(result)

        return None

    def _fetch_data(self, content, credits_content, **options):
        """
        fetches data from given content and credits content.

        :param bs4.BeautifulSoup content: the html content of imdb page.
        :param bs4.BeautifulSoup credits_content: the html content of credits page.

        :returns: list of actors.
        :rtype: list[dict]
        """

        cast_list_container = credits_content.find('table', class_='cast_list')
        stars = self._get_stars_imdb_page(content)
        actors = []
        if cast_list_container is not None:
            odd_rows = cast_list_container.find_all('tr', class_='odd')
            even_rows = cast_list_container.find_all('tr', class_='even')
            all_rows = []
            all_rows.extend(odd_rows)
            all_rows.extend(even_rows)
            for item in all_rows:
                fullname, imdb_page = self._get_fullname_and_imdb_page(item)
                character = self._get_character(item)
                photo_name = self._get_photo_url(item)
                single_actor = dict(fullname=fullname, imdb_page=imdb_page,
                                    character=character, photo_name=photo_name,
                                    is_star=imdb_page in stars)

                actors.append(single_actor)

        return actors or None


@updater()
class DirectorUpdater(PersonUpdaterBase):
    """
    director updater class.
    """

    _category = UpdaterCategoryEnum.DIRECTORS
