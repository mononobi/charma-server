# -*- coding: utf-8 -*-
"""
updater handlers content rate module.
"""

from bs4 import NavigableString

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBContentRateUpdater(UpdaterBase):
    """
    imdb content rate updater class.
    """

    _name = 'imdb_content_rate'
    _category = 'content_rate'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: update data
        """

        content_rate = None
        content_rate_container = content.find('div', class_='title_wrapper')
        if content_rate_container is not None:
            content_rate_tag = content_rate_container.find('div', class_='subtext')
            if content_rate_tag is not None and isinstance(content_rate_tag.next,
                                                           NavigableString):
                result = normalizer_services.filter(str(content_rate_tag.next),
                                                    filters=['\n'])
                if len(result) > 0:
                    content_rate = result

        return content_rate
