# -*- coding: utf-8 -*-
"""
updater handlers person module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase
from imovie.updater.handlers.mixin import IMDBHighQualityImageFetcherMixin


class PersonUpdaterBase(UpdaterBase, IMDBHighQualityImageFetcherMixin):
    """
    person updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: person information.
        :rtype: dict
        """
        pass


@updater()
class ActorUpdater(PersonUpdaterBase):
    """
    actor updater class.
    """

    _category = UpdaterCategoryEnum.ACTORS


@updater()
class DirectorUpdater(PersonUpdaterBase):
    """
    director updater class.
    """

    _category = UpdaterCategoryEnum.DIRECTORS
