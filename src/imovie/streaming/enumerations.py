# -*- coding: utf-8 -*-
"""
streaming providers enumerations module.
"""

from pyrin.core.enumerations import CoreEnum


class TranscoderPresetEnum(CoreEnum):
    """
    transcoder preset enum.

    lower presets have lower quality.
    """

    VERY_SLOW = 'very_slow'
    SLOW = 'slow'
    MEDIUM = 'medium'
    FAST = 'fast'
    ULTRA_FAST = 'ultrafast'


class VideoCodecEnum(CoreEnum):
    """
    video codec enum.
    """

    H263 = 'h263'
    H264 = 'h264'
    HEVC = 'hevc'


class AudioCodecEnum(CoreEnum):
    """
    audio codec enum.
    """

    AAC = 'aac'
    AC3 = 'ac3'
    MP3 = 'mp3'


class SubtitleCodecEnum(CoreEnum):
    """
    subtitle codec enum.
    """

    SRT = 'srt'
    MOV_TEXT = 'mov_text'
    SUBRIP = 'subrip'
    TEXT = 'text'


class FormatEnum(CoreEnum):
    """
    format enum.
    """

    DASH = 'dash'
    HLS = 'hls'


class TranscodingStatusEnum(CoreEnum):
    """
    transcoding status enum.
    """

    NOT_AVAILABLE = 'not_available'
    STARTED = 'started'
    FINISHED = 'finished'
    FAILED = 'failed'


class StreamProviderEnum(CoreEnum):
    """
    stream provider enum.
    """

    DASH = 'dash'
    HLS = 'hls'
