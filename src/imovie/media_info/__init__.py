# -*- coding: utf-8 -*-
"""
media info package.
"""

from pyrin.packaging.base import Package


class MediaInfoPackage(Package):
    """
    media info package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'media_info.component'
    CONFIG_STORE_NAMES = ['media.info']
