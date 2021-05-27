# -*- coding: utf-8 -*-
"""
streaming api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.streaming.services as streaming_services


@api('/stream/providers', authenticated=False)
def get_provider_names():
    """
    gets the name of all registered stream providers.

    :rtype: list[str]
    """

    return streaming_services.get_provider_names()


@api('/stream/<uuid:movie_id>', authenticated=False)
def start_stream(movie_id, **options):
    """
    starts streaming of given movie.

    it returns the related manifest file of the stream.

    :param uuid.UUID movie_id: movie id to be streamed.

    :keyword str subtitle: subtitle file path.
    :keyword int threads: number of threads to be used.
    :keyword str preset: transcoding preset name.

    :raises TranscodeError: transcode error.
    :raises StreamDoesNotExistError: stream does not exist error.

    :rtype: bytes
    """

    return streaming_services.start_stream(movie_id, **options)


@api('/stream/<uuid:movie_id>/<file>', authenticated=False)
def continue_stream(movie_id, file, **options):
    """
    continues the streaming of given movie id.

    :param uuid.UUID movie_id: movie id to be streamed.
    :param str file: stream file name to be returned.

    :raises StreamDoesNotExistError: stream does not exist error.

    :rtype: bytes
    """

    return streaming_services.continue_stream(movie_id, file, **options)
