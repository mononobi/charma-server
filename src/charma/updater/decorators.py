# -*- coding: utf-8 -*-
"""
updater decorators module.
"""

import charma.updater.services as updater_services


def updater(*args, **kwargs):
    """
    decorator to register an updater.

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


def processor(*args, **kwargs):
    """
    decorator to register an update processor.

    :param object args: processor class constructor arguments.
    :param object kwargs: processor class constructor keyword arguments.

    :raises InvalidProcessorTypeError: invalid processor type error.
    :raises DuplicateProcessorError: duplicate processor error.

    :returns: processor class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available processors.

        :param type cls: processor class.

        :returns: processor class.
        :rtype: type
        """

        instance = cls(*args, **kwargs)
        updater_services.register_processor(instance, **kwargs)

        return cls

    return decorator
