# -*- coding: utf-8 -*-
"""
media info decorators module.
"""

import imovie.media_info.services as media_info_services


def media_info_provider():
    """
    decorator to register a media info provider.

    :raises InvalidMediaInfoProviderTypeError: invalid media info provider type error.

    :returns: media info provider class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available media info providers.

        :param type cls: media info provider class.

        :returns: media info provider class.
        :rtype: type
        """

        instance = cls()
        media_info_services.register_provider(instance)

        return cls

    return decorator
