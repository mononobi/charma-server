# -*- coding: utf-8 -*-
"""
streaming component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.streaming import StreamingPackage
from imovie.streaming.manager import StreamingManager


@component(StreamingPackage.COMPONENT_NAME)
class StreamingComponent(Component, StreamingManager):
    """
    streaming component class.
    """
    pass
