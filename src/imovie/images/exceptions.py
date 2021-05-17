# -*- coding: utf-8 -*-
"""
images exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class ImagesException(CoreException):
    """
    images exception.
    """
    pass


class ImagesBusinessException(CoreBusinessException, ImagesException):
    """
    images business exception.
    """
    pass
