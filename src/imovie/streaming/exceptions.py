# -*- coding: utf-8 -*-
"""
streaming exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException, CoreNotFoundError


class StreamingException(CoreException):
    """
    streaming exception.
    """
    pass


class StreamingBusinessException(CoreBusinessException, StreamingException):
    """
    streaming business exception.
    """
    pass


class StreamDirectoryNotExistedError(StreamingBusinessException):
    """
    stream directory not existed error.
    """
    pass


class InvalidTranscodingStatusError(StreamingException):
    """
    invalid transcoding status error.
    """
    pass


class InvalidStreamProviderTypeError(StreamingException):
    """
    invalid stream provider type error.
    """
    pass


class DuplicateStreamProviderError(StreamingException):
    """
    duplicate stream provider error.
    """
    pass


class StreamProviderDoesNotExistError(StreamingBusinessException):
    """
    stream provider does not exist error.
    """
    pass


class TranscodeError(StreamingException):
    """
    transcode error.
    """
    pass


class StreamDoesNotExistError(CoreNotFoundError, StreamingBusinessException):
    """
    stream does not exist error.
    """
    pass
