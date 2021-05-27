# -*- coding: utf-8 -*-
"""
streaming providers dash module.
"""

from imovie.streaming.decorators import stream
from imovie.streaming.providers.base import StreamProviderBase
from imovie.streaming.enumerations import TranscoderPresetEnum, VideoCodecEnum, \
    AudioCodecEnum, SubtitleCodecEnum, FormatEnum, StreamProviderEnum


@stream()
class DASHStream(StreamProviderBase):
    """
    dash stream class.
    """

    _name = StreamProviderEnum.DASH
    _video_codec = VideoCodecEnum.H264
    _audio_codec = AudioCodecEnum.AAC
    _subtitle_codec = SubtitleCodecEnum.MOV_TEXT
    _default_preset = TranscoderPresetEnum.FAST
    _format = FormatEnum.DASH
    _default_threads = 2
    _output_file = 'dash.mpd'
