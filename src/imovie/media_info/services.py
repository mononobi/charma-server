# -*- coding: utf-8 -*-
"""
media info services module.
"""

from pyrin.application.services import get_component

from imovie.media_info import MediaInfoPackage


def register_provider(instance):
    """
    registers the given instance into media info providers.

    :param AbstractMediaInfoProvider instance: media info provider instance to be registered.

    :raises InvalidMediaInfoProviderTypeError: invalid media info provider type error.
    """

    return get_component(MediaInfoPackage.COMPONENT_NAME).register_provider(instance)


def get_info(file, **options):
    """
    gets a dict containing media info of given file.

    :param str file: absolute path of video file.

    :returns: dict(int runtime,
                   int width,
                   int height)

    :rtype: dict
    """

    return get_component(MediaInfoPackage.COMPONENT_NAME).get_info(file, **options)
