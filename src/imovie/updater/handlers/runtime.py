# -*- coding: utf-8 -*-
"""
updater handlers runtime module.
"""

import re

import pyrin.utilities.string.normalizer.services as normalizer_services

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


class RuntimeUpdaterBase(UpdaterBase):
    """
    runtime updater base class.
    """

    _category = UpdaterCategoryEnum.RUNTIME


@updater()
class RuntimeUpdater(RuntimeUpdaterBase):
    """
    runtime updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb runtime.
        :rtype: int
        """

        runtime = None
        runtime_tag = content.find('time', datetime=True)
        if runtime_tag is not None:
            result = runtime_tag.get('datetime')
            result = normalizer_services.filter(result, filters=['PT', 'M'])
            if result.isdigit():
                runtime = int(result)

        return runtime


@updater()
class RuntimeUpdaterV2(RuntimeUpdaterBase):
    """
    runtime updater v2 class.
    """

    RUNTIME_REGEX = re.compile(r'^(\d+h)( \d+min)?$|^(\d+min)$', re.IGNORECASE)

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb runtime.
        :rtype: int
        """

        runtime = None
        metadata_list = content.find('ul', {'data-testid': 'hero-title-block__metadata'})
        if metadata_list is not None:
            potential_runtimes = metadata_list.find_all('li')
            reversed_runtimes = reversed(potential_runtimes)
            for item in reversed_runtimes:
                value = self._get_runtime(item.get_text(strip=True))
                if value is not None:
                    runtime = value
                    break

        return runtime

    def _get_runtime(self, text):
        """
        gets the runtime in minutes from given text.

        it may return None if runtime could not be extracted.

        :param str text: text to extract runtime from it.

        :rtype: int
        """

        runtime = None
        matched = re.match(self.RUNTIME_REGEX, text)
        if matched:
            total = 0
            hour, minutes, only_minutes = matched.groups()
            hour = normalizer_services.filter(hour, filters=['h'])
            minutes = normalizer_services.filter(minutes, filters=['min'])
            only_minutes = normalizer_services.filter(only_minutes, filters=['min'])
            if hour is not None and hour.isdigit():
                total += int(hour) * 60

            if minutes is not None and minutes.isdigit():
                total += int(minutes)

            if only_minutes is not None and only_minutes.isdigit():
                total += int(only_minutes)

            if total > 0:
                runtime = total

        return runtime
