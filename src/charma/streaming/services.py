# -*- coding: utf-8 -*-
"""
streaming services module.
"""

from pyrin.application.services import get_component

from charma.streaming import StreamingPackage


def register_stream_provider(instance, **options):
    """
    registers the given stream provider.

    :param AbstractStreamProvider instance: stream provider instance.

    :raises InvalidStreamProviderTypeError: invalid stream provider type error.
    :raises DuplicateStreamProviderError: duplicate stream provider error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).register_stream_provider(instance,
                                                                                   **options)


def get_provider_names():
    """
    gets the name of all registered stream providers.

    :rtype: list[str]
    """

    return get_component(StreamingPackage.COMPONENT_NAME).get_provider_names()


def exists(directory):
    """
    gets a value indicating that given stream directory exists.

    :param str directory: directory path of stream.

    :raises InvalidPathError: invalid path error.
    :raises PathIsNotAbsoluteError: path is not absolute error.

    :rtype: bool
    """

    return get_component(StreamingPackage.COMPONENT_NAME).exists(directory)


def get_status(directory):
    """
    gets the transcoding status of given stream directory.

    :param str directory: directory path of stream.

    :rtype: str
    """

    return get_component(StreamingPackage.COMPONENT_NAME).get_status(directory)


def set_started(directory):
    """
    sets the given stream as started transcoding.

    :param str directory: directory path of stream.

    :raises StreamDirectoryNotExistedError: stream directory not existed error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).set_started(directory)


def set_finished(directory):
    """
    sets the given stream as finished transcoding.

    :param str directory: directory path of stream.

    :raises StreamDirectoryNotExistedError: stream directory not existed error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).set_finished(directory)


def set_failed(directory, error):
    """
    sets the given stream as failed transcoding.

    :param str directory: directory path of stream.
    :param str error: error message.

    :raises StreamDirectoryNotExistedError: stream directory not existed error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).set_failed(directory, error)


def set_process_id(directory, process_id):
    """
    sets the ffmpeg process id for given stream.

    :param str directory: directory path of stream.
    :param int process_id: ffmpeg process id.

    :raises StreamDirectoryNotExistedError: stream directory not existed error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).set_process_id(directory,
                                                                         process_id)


def set_access_time(directory):
    """
    sets the last access time for given stream.

    :param str directory: directory path of stream.

    :raises StreamDirectoryNotExistedError: stream directory not existed error.
    """

    return get_component(StreamingPackage.COMPONENT_NAME).set_access_time(directory)


def start_stream(movie_id, **options):
    """
    starts streaming of given movie.

    it returns the related manifest file of the stream.

    :param uuid.UUID movie_id: movie id to be streamed.

    :raises MovieDirectoryNotFoundError: movie directory not found error.
    :raises MultipleMovieDirectoriesFoundError: multiple movie directories found error.
    :raises MovieFileNotFoundError: movie file not found error.
    :raises MultipleMovieFilesFoundError: multiple movie files found error.
    :raises StreamDoesNotExistError: stream does not exist error.

    :rtype: bytes
    """

    return get_component(StreamingPackage.COMPONENT_NAME).start_stream(movie_id, **options)


def continue_stream(movie_id, file, **options):
    """
    continues the streaming of given movie.

    :param uuid.UUID movie_id: movie id to be streamed.
    :param str file: stream file name to be returned.

    :raises StreamDoesNotExistError: stream does not exist error.

    :rtype: bytes
    """

    return get_component(StreamingPackage.COMPONENT_NAME).continue_stream(movie_id, file,
                                                                          **options)
