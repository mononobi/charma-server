# -*- coding: utf-8 -*-
"""
search manager module.
"""

from pyrin.core.structs import Manager, Context

from imovie.search import SearchPackage
from imovie.search.interface import AbstractSearchProvider
from imovie.search.exceptions import InvalidSearchProviderTypeError, \
    DuplicateSearchProviderError, SearchProviderCategoryNotFoundError, \
    SearchProviderNotFoundError


class SearchManager(Manager):
    """
    search manager class.
    """

    package_class = SearchPackage

    def __init__(self):
        """
        initializes an instance of SearchManager.
        """

        super().__init__()

        # a dict containing all search providers. in the form of:
        # {str category: {str name: AbstractSearchProvider provider}}
        self._providers = Context()

    def _get_providers(self, category, **options):
        """
        gets a dict of all search providers of given category.

        :param str category: category name.

        :raises SearchProviderCategoryNotFoundError: search provider category not found error.

        :rtype: dict[str, AbstractSearchProvider]
        """

        if category not in self._providers:
            raise SearchProviderCategoryNotFoundError('Search provider category [{category}] '
                                                      'not found.'.format(category=category))

        return self._providers.get(category)

    def register_provider(self, instance, **options):
        """
        registers the given provider into available search providers.

        :param AbstractSearchProvider instance: search provider to be registered.

        :raises InvalidSearchProviderTypeError: invalid search provider type error.
        :raises DuplicateSearchProviderError: duplicate search provider error.
        """

        if not isinstance(instance, AbstractSearchProvider):
            raise InvalidSearchProviderTypeError('Input parameter [{instance}] is '
                                                 'not an instance of [{base}].'
                                                 .format(instance=instance,
                                                         base=AbstractSearchProvider))

        providers = self._providers.get(instance.category) or {}
        if instance.name in providers:
            raise DuplicateSearchProviderError('There is another registered search provider '
                                               'with name [{name}] and category [{category}].'
                                               .format(name=instance.name,
                                                       category=instance.category))

        providers[instance.name] = instance
        self._providers[instance.category] = providers

    def get_provider(self, category, name, **options):
        """
        gets a search provider of given category with given name.

        :param str category: category name.
        :param str name: search provider name.

        :raises SearchProviderNotFoundError: search provider not found error.

        :rtype: AbstractSearchProviders
        """

        providers = self._get_providers(category, **options)
        if name not in providers:
            raise SearchProviderNotFoundError('Search provider with name [{name}] '
                                              'not found in category [{category}].'
                                              .format(name=name, category=category))

        return providers.get(name)

    def get_providers(self, category, **options):
        """
        gets a list of all search providers of given category.

        :param str category: category name.

        :raises SearchProviderCategoryNotFoundError: search provider category not found error.

        :rtype: list[AbstractSearchProvider]
        """

        providers = self._get_providers(category, **options)
        return list(providers.values())

    def search(self, text, category, **options):
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

        result = None
        providers = self.get_providers(category)
        for item in providers:
            result = item.search(text, **options)
            if result is not None:
                break

        return result
