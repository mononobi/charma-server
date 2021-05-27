# -*- coding: utf-8 -*-
"""
streaming providers hls module.
"""

from imovie.streaming.decorators import stream
from imovie.streaming.providers.base import StreamProviderBase
from imovie.streaming.enumerations import TranscoderPresetEnum, VideoCodecEnum, \
    AudioCodecEnum, SubtitleCodecEnum, FormatEnum, StreamProviderEnum


@stream()
class HLSStream(StreamProviderBase):
    """
    hls stream class.
    """

    _name = StreamProviderEnum.HLS
    _video_codec = VideoCodecEnum.H264
    _audio_codec = AudioCodecEnum.AAC
    _subtitle_codec = SubtitleCodecEnum.MOV_TEXT
    _default_preset = TranscoderPresetEnum.FAST
    _format = FormatEnum.HLS
    _default_threads = 2
    _output_file = 'hls.m3u8'
