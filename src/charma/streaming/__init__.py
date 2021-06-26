# -*- coding: utf-8 -*-
"""
streaming package.
"""

from pyrin.packaging.base import Package


class StreamingPackage(Package):
    """
    streaming package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'streaming.component'
    CONFIG_STORE_NAMES = ['streaming']
