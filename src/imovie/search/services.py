# -*- coding: utf-8 -*-
"""
search services module.
"""

from pyrin.application.services import get_component

from imovie.search import SearchPackage


def register_provider(instance, **options):
    """
    registers the given provider into available search providers.

    :param AbstractSearchProvider instance: search provider to be registered.

    :raises InvalidSearchProviderTypeError: invalid search provider type error.
    :raises DuplicateSearchProviderError: duplicate search provider error.
    """

    return get_component(SearchPackage.COMPONENT_NAME).register_provider(instance, **options)


def get_provider(category, name, **options):
    """
    gets a search provider of given category with given name.

    :param str category: category name.
    :param str name: search provider name.

    :raises SearchProviderNotFoundError: search provider not found error.

    :rtype: AbstractSearchProviders
    """

    return get_component(SearchPackage.COMPONENT_NAME).get_provider(category, name, **options)


def get_providers(category, **options):
    """
    gets a list of all search providers of given category.

    :param str category: category name.

    :raises SearchProviderCategoryNotFoundError: search provider category not found error.

    :rtype: list[AbstractSearchProvider]
    """

    return get_component(SearchPackage.COMPONENT_NAME).get_providers(category, **options)


def search(text, category, **options):
    """
    searches given text for given category and returns a url.

    it may return None if nothing found.

    :param str text: text to be searched for.
    :param str category: category of search providers to be used.

    :keyword int limit: max number of urls to be tried before giving
                        up the search. defaults to 5 if not provided.
                        it could not be more than 10.

    :raises SearchProviderCategoryNotFoundError: search provider category not found error.
    """

    return get_component(SearchPackage.COMPONENT_NAME).search(text, category, **options)
