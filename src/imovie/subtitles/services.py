# -*- coding: utf-8 -*-
"""
subtitles services module.
"""

from pyrin.application.services import get_component

from imovie.subtitles import SubtitlesPackage


def get_subtitles(directory):
    """
    gets all subtitle files in given directory.

    :param str directory: directory to get subtitles from.

    :rtype: list[str]
    """

    return get_component(SubtitlesPackage.COMPONENT_NAME).get_subtitles(directory)
