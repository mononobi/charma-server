# -*- coding: utf-8 -*-
"""
downloader package.
"""

from pyrin.packaging.base import Package


class DownloaderPackage(Package):
    """
    downloader package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'downloader.component'
    CONFIG_STORE_NAMES = ['downloader']
