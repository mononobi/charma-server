# -*- coding: utf-8 -*-
"""
media info handlers exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class MediaInfoHandlersException(CoreException):
    """
    media info handlers exception.
    """
    pass


class MediaInfoHandlersBusinessException(CoreBusinessException,
                                         MediaInfoHandlersException):
    """
    media info handlers business exception.
    """
    pass
