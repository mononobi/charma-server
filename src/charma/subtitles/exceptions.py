# -*- coding: utf-8 -*-
"""
subtitles exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class SubtitlesException(CoreException):
    """
    subtitles exception.
    """
    pass


class SubtitlesBusinessException(CoreBusinessException, SubtitlesException):
    """
    subtitles business exception.
    """
    pass
