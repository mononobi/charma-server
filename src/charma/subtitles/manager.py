# -*- coding: utf-8 -*-
"""
subtitles manager module.
"""

import pyrin.utils.path as path_utils

from pyrin.core.structs import Manager

from charma.subtitles import SubtitlesPackage


class SubtitlesManager(Manager):
    """
    subtitles manager class.
    """

    package_class = SubtitlesPackage

    # all supported subtitle file extensions.
    SUBTITLE_EXTENSIONS = ('srt',)

    def get_subtitles(self, directory):
        """
        gets all subtitle files in given directory.

        :param str directory: directory to get subtitles from.

        :rtype: list[str]
        """

        return path_utils.get_files(directory, *self.SUBTITLE_EXTENSIONS)
