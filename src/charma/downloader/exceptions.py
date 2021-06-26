# -*- coding: utf-8 -*-
"""
downloader exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class DownloaderException(CoreException):
    """
    downloader exception.
    """
    pass


class DownloaderBusinessException(CoreBusinessException, DownloaderException):
    """
    downloader business exception.
    """
    pass
