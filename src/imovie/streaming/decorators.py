# -*- coding: utf-8 -*-
"""
streaming decorators module.
"""

import imovie.streaming.services as streaming_services


def stream(*args, **kwargs):
    """
    decorator to register a stream provider.

    :param object args: stream provider class constructor arguments.
    :param object kwargs: stream provider class constructor keyword arguments.

    :raises InvalidStreamProviderTypeError: invalid stream provider type error.
    :raises DuplicateStreamProviderError: duplicate stream provider error.

    :returns: stream provider class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available stream providers.

        :param type cls: stream provider class.

        :returns: stream provider class.
        :rtype: type
        """

        instance = cls(*args, **kwargs)
        streaming_services.register_stream_provider(instance, **kwargs)

        return cls

    return decorator
