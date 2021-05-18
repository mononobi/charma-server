# -*- coding: utf-8 -*-
"""
updater handlers movie poster module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase
from imovie.updater.handlers.mixin import IMDBHighQualityImageFetcherMixin


@updater()
class MoviePosterUpdater(UpdaterBase, IMDBHighQualityImageFetcherMixin):
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
        """

        image_url = None
        url_container = content.find('div', class_='title-overview')
        if url_container is not None:
            poster_tag = url_container.find('div', class_='poster')
            if poster_tag is not None:
                image_tag = poster_tag.find('img', src=True)
                if image_tag is not None:
                    result = image_tag.get('src')
                    if result is not None:
                        image_url = self.get_high_quality_image_url(result)

        return image_url
