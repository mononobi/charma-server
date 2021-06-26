# -*- coding: utf-8 -*-
"""
downloader services module.
"""

from pyrin.application.services import get_component

from charma.downloader import DownloaderPackage


def download(url, target, **options):
    """
    downloads the file from given url and saves it to target path.

    it returns a tuple of two items. first item is the full path of
    downloaded file and the second item is the name of the downloaded file.

    :param str url: file url to be downloaded.
    :param str target: absolute target path to save the downloaded file.

    :keyword str name: file name to be saved with.

    :returns: tuple[str full_path, str name]
    :rtype: tuple[str, str]
    """

    return get_component(DownloaderPackage.COMPONENT_NAME).download(url, target, **options)


def get_unique_file_name(target, name, **options):
    """
    gets a unique file name in given target path.

    if the same file is already existed, it uses the digit slug generator
    to produce a slug and append it to the original requested name.

    :param str target: absolute target path to save the file.
    :param str name: file name to be used.

    :rtype: str
    """

    return get_component(DownloaderPackage.COMPONENT_NAME).get_unique_file_name(target,
                                                                                name,
                                                                                **options)
