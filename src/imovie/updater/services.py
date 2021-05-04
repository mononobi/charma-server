# -*- coding: utf-8 -*-
"""
updater services module.
"""

from pyrin.application.services import get_component

from imovie.updater import UpdaterPackage


def register_updater(instance, **options):
    """
    registers a new updater.

    :param AbstractUpdater instance: updater to be registered.
                                     it must be an instance of
                                     AbstractUpdater.

    :raises InvalidUpdaterTypeError: invalid updater type error.
    :raises DuplicateUpdaterError: duplicate updater error.
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).register_updater(instance, **options)


def get_updater(category, **options):
    """
    gets the first element of chained updaters for given category.

    :param str category: category name.

    :raises UpdaterCategoryNotFoundError: updater category not found error.

    :rtype: AbstractUpdater
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).get_updater(category, **options)


def fetch(url, category, **options):
    """
    fetches data from given url for given category.

    it may return None if no data is available.

    :param str url: url to fetch data from it.
    :param str category: category of updaters to be used.

    :keyword bs4.BeautifulSoup content: the html content of input url.

    :raises UpdaterCategoryNotFoundError: updater category not found error.
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).fetch(url, category, **options)
