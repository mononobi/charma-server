# -*- coding: utf-8 -*-
"""
media info component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.media_info import MediaInfoPackage
from imovie.media_info.manager import MediaInfoManager


@component(MediaInfoPackage.COMPONENT_NAME)
class MediaInfoComponent(Component, MediaInfoManager):
    """
    media info component class.
    """
    pass
