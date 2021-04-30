# -*- coding: utf-8 -*-
"""
search decorators module.
"""

import imovie.search.services as search_services


def search_provider(*args, **kwargs):
    """
    decorator to register a search provider.

    :param object args: search provider class constructor arguments.
    :param object kwargs: search provider class constructor keyword arguments.

    :raises InvalidSearchProviderTypeError: invalid search provider type error.
    :raises DuplicateSearchProviderError: duplicate search provider error.

    :returns: search provider class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available search providers.

        :param type cls: search provider class.

        :returns: search provider class.
        :rtype: type
        """

        instance = cls(*args, **kwargs)
        search_services.register_provider(instance, **kwargs)

        return cls

    return decorator
