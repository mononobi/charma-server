# -*- coding: utf-8 -*-
"""
updater handlers runtime module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class RuntimeUpdater(UpdaterBase):
    """
    runtime updater class.
    """

    _category = UpdaterCategoryEnum.RUNTIME

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb runtime.
        """

        runtime = None
        runtime_tag = content.find('time', datetime=True)
        if runtime_tag is not None:
            result = runtime_tag.get('datetime')
            result = normalizer_services.filter(result, filters=['PT', 'M'])
            if result.isdigit():
                runtime = int(result)

        return runtime
