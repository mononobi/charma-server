# -*- coding: utf-8 -*-
"""
actors exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ActorsException(CoreException):
    """
    actors exception.
    """
    pass


class ActorsBusinessException(CoreBusinessException, ActorsException):
    """
    actors business exception.
    """
    pass


class ActorDoesNotExistError(ActorsBusinessException):
    """
    actor does not exist error.
    """
    pass


class InvalidActorHookTypeError(ActorsException):
    """
    invalid actor hook type error.
    """
    pass
