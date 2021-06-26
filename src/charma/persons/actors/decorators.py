# -*- coding: utf-8 -*-
"""
actors decorators module.
"""

import charma.persons.actors.services as actor_services


def actor_hook():
    """
    decorator to register an actor hook.

    :raises InvalidActorHookTypeError: invalid actor hook type error.

    :returns: actor hook class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available actor hooks.

        :param type cls: actor hook class.

        :returns: actor hook class.
        :rtype: type
        """

        instance = cls()
        actor_services.register_hook(instance)

        return cls

    return decorator
