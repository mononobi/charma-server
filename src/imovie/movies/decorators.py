# -*- coding: utf-8 -*-
"""
movies decorator module.
"""

import imovie.movies.services as movie_services


def movie_hook():
    """
    decorator to register a movie hook.

    :raises InvalidMovieHookTypeError: invalid movie hook type error.

    :returns: movie hook class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available movie hooks.

        :param type cls: movie hook class.

        :returns: movie hook class.
        :rtype: type
        """

        instance = cls()
        movie_services.register_hook(instance)

        return cls

    return decorator
