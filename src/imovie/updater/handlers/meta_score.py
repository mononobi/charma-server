# -*- coding: utf-8 -*-
"""
updater handlers meta score module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class MetaScoreUpdater(UpdaterBase):
    """
    meta score class.
    """

    _category = UpdaterCategoryEnum.META_SCORE

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb meta score.
        """

        meta_score = None
        meta_score_container = content.find(
            'div', class_='metacriticScore score_favorable titleReviewBarSubItem')

        if meta_score_container is not None:
            meta_score_tag = meta_score_container.find('span')
            if meta_score_tag is not None:
                result = meta_score_tag.get_text(strip=True)
                if result.isdigit():
                    meta_score = int(result)

        return meta_score
