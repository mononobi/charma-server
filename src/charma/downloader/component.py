# -*- coding: utf-8 -*-
"""
downloader component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from charma.downloader import DownloaderPackage
from charma.downloader.manager import DownloaderManager


@component(DownloaderPackage.COMPONENT_NAME)
class DownloaderComponent(Component, DownloaderManager):
    """
    downloader component class.
    """
    pass
