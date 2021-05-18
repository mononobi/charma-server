# -*- coding: utf-8 -*-
"""
updater handlers meta score module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


class MetaScoreUpdaterBase(UpdaterBase):
    """
    meta score updater base class.
    """

    _category = UpdaterCategoryEnum.META_SCORE
    _META_SCORE_CONTAINER_CLASS = None

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb meta score.
        :rtype: int
        """

        meta_score = None
        meta_score_container = content.find('div', class_=self._META_SCORE_CONTAINER_CLASS)
        if meta_score_container is not None:
            meta_score_tag = meta_score_container.find('span')
            if meta_score_tag is not None:
                result = meta_score_tag.get_text(strip=True)
                if result.isdigit():
                    meta_score = int(result)

        return meta_score


@updater()
class MetaScoreUpdaterHigh(MetaScoreUpdaterBase):
    """
    meta score updater high class.
    """

    _category = UpdaterCategoryEnum.META_SCORE
    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_favorable titleReviewBarSubItem'


@updater()
class MetaScoreUpdaterMiddle(MetaScoreUpdaterBase):
    """
    meta score updater middle class.
    """

    _category = UpdaterCategoryEnum.META_SCORE
    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_mixed titleReviewBarSubItem'


@updater()
class MetaScoreUpdaterLow(MetaScoreUpdaterBase):
    """
    meta score updater low class.
    """

    _category = UpdaterCategoryEnum.META_SCORE
    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_unfavorable titleReviewBarSubItem'
