# -*- coding: utf-8 -*-
"""
subtitles component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from imovie.subtitles import SubtitlesPackage
from imovie.subtitles.manager import SubtitlesManager


@component(SubtitlesPackage.COMPONENT_NAME)
class SubtitlesComponent(Component, SubtitlesManager):
    """
    subtitles component class.
    """
    pass
