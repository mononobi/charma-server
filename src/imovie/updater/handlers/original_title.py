# -*- coding: utf-8 -*-
"""
updater handlers original title module.
"""

from bs4 import NavigableString

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBOriginalTitleUpdater(UpdaterBase):
    """
    imdb original title updater class.
    """

    _name = 'imdb_original_title'
    _category = 'original_title'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb original title.
        """

        original_title = None
        original_title_tag = content.find('div', class_='originalTitle')
        if original_title_tag is not None and isinstance(original_title_tag.next,
                                                         NavigableString):
            result = normalizer_services.filter(str(original_title_tag.next),
                                                filters=['\n'])
            if len(result) > 0:
                original_title = result

        return original_title
