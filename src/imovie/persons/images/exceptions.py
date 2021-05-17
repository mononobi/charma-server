# -*- coding: utf-8 -*-
"""
persons images exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class PersonsImagesException(CoreException):
    """
    persons images exception.
    """
    pass


class PersonsImagesBusinessException(CoreBusinessException, PersonsImagesException):
    """
    persons images business exception.
    """
    pass
