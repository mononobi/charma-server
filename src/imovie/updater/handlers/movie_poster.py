# -*- coding: utf-8 -*-
"""
updater handlers movie poster module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase
from imovie.updater.handlers.mixin import ImageSetFetcherMixin


@updater()
class MoviePosterUpdater(UpdaterBase):
    """
    movie poster updater class.
    """

    _category = UpdaterCategoryEnum.POSTER_NAME

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
                    image_url = image_tag.get('src') or None

        return image_url


@updater()
class MoviePosterUpdaterV2(UpdaterBase, ImageSetFetcherMixin):
    """
    movie poster updater v2 class.
    """

    _category = UpdaterCategoryEnum.POSTER_NAME

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
            image_tag = url_container.find('img', srcset=True)
            if image_tag is not None:
                image_url = self.get_highest_quality_image_url(image_tag.get('srcset'))

        return image_url
