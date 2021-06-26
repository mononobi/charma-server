# -*- coding: utf-8 -*-
"""
directors decorators module.
"""

import charma.persons.directors.services as director_services


def director_hook():
    """
    decorator to register a director hook.

    :raises InvalidDirectorHookTypeError: invalid director hook type error.

    :returns: director hook class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available director hooks.

        :param type cls: director hook class.

        :returns: director hook class.
        :rtype: type
        """

        instance = cls()
        director_services.register_hook(instance)

        return cls

    return decorator
