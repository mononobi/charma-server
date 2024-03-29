# -*- coding: utf-8 -*-
"""
updater handlers meta score module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class MetaScoreUpdaterBase(UpdaterBase):
    """
    meta score updater base class.
    """

    _category = UpdaterCategoryEnum.META_SCORE


class MetaScoreUpdater(MetaScoreUpdaterBase):
    """
    meta score updater class.
    """

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
class MetaScoreUpdaterHigh(MetaScoreUpdater):
    """
    meta score updater high class.
    """

    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_favorable titleReviewBarSubItem'


@updater()
class MetaScoreUpdaterMiddle(MetaScoreUpdater):
    """
    meta score updater middle class.
    """

    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_mixed titleReviewBarSubItem'


@updater()
class MetaScoreUpdaterLow(MetaScoreUpdater):
    """
    meta score updater low class.
    """

    _META_SCORE_CONTAINER_CLASS = 'metacriticScore score_unfavorable titleReviewBarSubItem'


@updater()
class MetaScoreUpdaterV2(MetaScoreUpdaterBase):
    """
    meta score updater v2 class.
    """

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
        meta_score_tag = content.find('span', class_='score-meta')
        if meta_score_tag is not None:
            result = meta_score_tag.get_text(strip=True)
            if result.isdigit():
                meta_score = int(result)

        return meta_score
