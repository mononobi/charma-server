# -*- coding: utf-8 -*-
"""
updater handlers movie poster module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase
from charma.updater.handlers.mixin import ImageFetcherMixin


class MoviePosterUpdaterBase(UpdaterBase, ImageFetcherMixin):
    """
    movie poster updater base class.
    """

    _category = UpdaterCategoryEnum.POSTER_NAME
    IMAGE_WIDTH = 380
    IMAGE_HEIGHT = 562


@updater()
class MoviePosterUpdater(MoviePosterUpdaterBase):
    """
    movie poster updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb movie poster url.
        :rtype: str
        """

        image_url = None
        url_container = content.find('div', class_='title-overview')
        if url_container is not None:
            poster_tag = url_container.find('div', class_='poster')
            if poster_tag is not None:
                image_tag = poster_tag.find('img', src=True)
                if image_tag is not None:
                    image_url = self.get_resized_image_url(image_tag.get('src'),
                                                           self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        return image_url


@updater()
class MoviePosterUpdaterV2(MoviePosterUpdaterBase):
    """
    movie poster updater v2 class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb movie poster url.
        :rtype: str
        """

        image_url = None
        url_container = content.find('div', {'data-testid': 'hero-media__poster'})
        if url_container is not None:
            image_tag = url_container.find('img', src=True)
            if image_tag is not None:
                image_url = self.get_resized_image_url(image_tag.get('src'),
                                                       self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        return image_url
