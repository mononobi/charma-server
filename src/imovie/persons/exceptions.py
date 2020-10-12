# -*- coding: utf-8 -*-
"""
persons exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class PersonsException(CoreException):
    """
    persons exception.
    """
    pass


class PersonsBusinessException(CoreBusinessException, PersonsException):
    """
    persons business exception.
    """
    pass
