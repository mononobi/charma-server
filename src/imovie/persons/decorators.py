# -*- coding: utf-8 -*-
"""
persons decorator module.
"""

import imovie.persons.services as person_services


def person_handler(*args, **kwargs):
    """
    decorator to register a person handler.

    :param object args: handler class constructor arguments.
    :param object kwargs: handler class constructor keyword arguments.

    :raises InvalidPersonHandlerTypeError: invalid person handler type error.
    :raises PersonHandlerNameRequiredError: person handler name required error.
    :raises DuplicatedPersonHandlerError: duplicated person handler error.

    :returns: handler class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available person handlers.

        :param type cls: handler class.

        :returns: handler class.
        :rtype: type
        """

        instance = cls(*args, **kwargs)
        person_services.register_handler(instance, **kwargs)

        return cls

    return decorator


def person_hook():
    """
    decorator to register a person hook.

    :raises InvalidPersonHookTypeError: invalid person hook type error.

    :returns: person hook class.
    :rtype: type
    """

    def decorator(cls):
        """
        decorates the given class and registers an instance
        of it into available person hooks.

        :param type cls: person hook class.

        :returns: person hook class.
        :rtype: type
        """

        instance = cls()
        person_services.register_hook(instance)

        return cls

    return decorator
