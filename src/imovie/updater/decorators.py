# -*- coding: utf-8 -*-
"""
updater decorators module.
"""

import imovie.updater.services as updater_services


def updater(*args, **kwargs):
    """
    decorator to register a updater.

    :param object args: updater class constructor arguments.
    :param object kwargs: updater class constructor keyword arguments.

    :raises InvalidUpdaterTypeError: invalid updater type error.
    :raises DuplicateUpdaterError: duplicate updater error.

    :returns: updater class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available updaters.

        :param type cls: updater class.

        :returns: updater class.
        :rtype: type
        """

        instance = cls(*args, **kwargs)
        updater_services.register_updater(instance, **kwargs)

        return cls

    return decorator
