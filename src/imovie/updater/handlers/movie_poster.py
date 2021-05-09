# -*- coding: utf-8 -*-
"""
updater handlers movie poster module.
"""

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase
from imovie.updater.handlers.mixin import IMDBHighQualityImageFetcherMixin


@updater()
class IMDBMoviePosterUpdater(UpdaterBase, IMDBHighQualityImageFetcherMixin):
    """
    imdb movie poster updater class.
    """

    _name = 'imdb_movie_poster'
    _category = 'movie_poster'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb movie poster url.
        """

        url = None
        url_container = content.find('div', class_='title-overview')
        if url_container is not None:
            poster_tag = url_container.find('div', class_='poster')
            if poster_tag is not None:
                image_tag = poster_tag.find('img', src=True)
                if image_tag is not None:
                    result = image_tag.get('src')
                    if result is not None:
                        url = self.get_high_quality_image_url(result)

        return url
