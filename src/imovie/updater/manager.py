# -*- coding: utf-8 -*-
"""
updater manager module.
"""

from collections import OrderedDict

from pyrin.core.structs import Manager, Context

import imovie.scraper.services as scraper_services

from imovie.updater import UpdaterPackage
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.interface import AbstractUpdater
from imovie.updater.exceptions import InvalidUpdaterTypeError, DuplicateUpdaterError, \
    UpdaterCategoryNotFoundError


class UpdaterManager(Manager):
    """
    updater manager class.
    """

    package_class = UpdaterPackage

    def __init__(self):
        """
        initializes an instance of UpdaterManager.
        """

        super().__init__()

        # a dict containing all updater handlers for each category. in the form of:
        # {str category: {str name: AbstractUpdater updater}}
        self._updaters = Context()

    def _get_updaters(self, category, **options):
        """
        gets a dict of all updaters of given category.

        :param str category: category name.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :rtype: dict[str, AbstractUpdater]
        """

        if category not in self._updaters:
            raise UpdaterCategoryNotFoundError('Updater category [{category}] not '
                                               'found.'.format(category=category))

        return self._updaters.get(category)

    def _set_next_handlers(self, updaters):
        """
        sets next handler for each updater in the input list.

        :param dict[str, AbstractUpdater] updaters: dict of updaters.
        """

        instances = list(updaters.values())
        length = len(updaters)
        for i in range(length):
            if i == length - 1:
                instances[i].set_next(None)
            else:
                instances[i].set_next(instances[i + 1])

    def register_updater(self, instance, **options):
        """
        registers a new updater.

        :param AbstractUpdater instance: updater to be registered.
                                         it must be an instance of
                                         AbstractUpdater.

        :raises InvalidUpdaterTypeError: invalid updater type error.
        :raises DuplicateUpdaterError: duplicate updater error.
        """

        if not isinstance(instance, AbstractUpdater):
            raise InvalidUpdaterTypeError('Input parameter [{instance}] is '
                                          'not an instance of [{base}].'
                                          .format(instance=instance,
                                                  base=AbstractUpdater))

        previous_instances = self._updaters.get(instance.category, OrderedDict())
        if instance.category in self._updaters and instance.name in previous_instances:
            raise DuplicateUpdaterError('There is another registered updater with '
                                        'name [{name}] and category [{category}].'
                                        .format(name=instance.name,
                                                category=instance.category))

        previous_instances[instance.name] = instance
        self._set_next_handlers(previous_instances)
        self._updaters[instance.category] = previous_instances

    def get_updater(self, category, **options):
        """
        gets the first element of chained updaters for given category.

        :param str category: category name.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :rtype: AbstractUpdater
        """

        updaters = self._get_updaters(category, **options)
        updaters = list(updaters.values())
        return updaters[0]

    def fetch(self, url, category, **options):
        """
        fetches data from given url for given category.

        it may return None if no data is available.

        :param str url: url to fetch data from it.
        :param str category: category of updaters to be used.

        :keyword bs4.BeautifulSoup content: the html content of input url.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :returns: dict[str category, object value]
        :rtype: dict
        """

        updater = self.get_updater(category, **options)
        result = updater.fetch(url, **options)
        if result is None:
            return None

        final_result = dict()
        final_result[updater.category] = result
        return final_result

    def fetch_all(self, url, *categories, **options):
        """
        fetches data from given url for specified categories.

        :param str url: url to fetch data from it.

        :param str categories: categories of updaters to be used.
                               if not provided, all categories will be used.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :returns: a dict of all updated values and their categories.
        :rtype: dict
        """

        content = scraper_services.get(url, **options)
        options.update(content=content)
        categories = set(categories)
        if len(categories) <= 0:
            categories = UpdaterCategoryEnum.values()

        final_result = dict()
        for item in categories:
            result = self.fetch(url, item, **options)
            if result is not None:
                final_result.update(result)

        return final_result
