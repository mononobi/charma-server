# -*- coding: utf-8 -*-
"""
downloader manager module.
"""

import os

import pyrin.utils.path as path_utils
import pyrin.utils.slug as slug_utils

from pyrin.core.structs import Manager

import charma.scraper.services as scraper_services

from charma.downloader import DownloaderPackage


class DownloaderManager(Manager):
    """
    downloader manager class.
    """

    package_class = DownloaderPackage

    # this slug will be appended to file name when a file
    # with the same name is already existed.
    SEQUENCE_SLUG = ' -D{digits}'

    def _get_sequence_slug(self):
        """
        gets a sequence slug to be used if a file with the same name is already existed.

        :rtype: str
        """

        digits = slug_utils.get_digit_slug(6)
        return self.SEQUENCE_SLUG.format(digits=digits)

    def download(self, url, target, **options):
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

        name = options.get('name')
        original_name = path_utils.get_file_name(url)
        extension = path_utils.get_file_extension(url, remove_dot=False, lowercase=False)
        if name is not None:
            name = '{name}{extension}'.format(name=name, extension=extension)
            original_name = name

        unique_name = self.get_unique_file_name(target, original_name)
        fullname = os.path.join(target, unique_name)
        response = scraper_services.get(url)
        with open(fullname, mode='wb') as file:
            file.write(response.content)

        return fullname, unique_name

    def get_unique_file_name(self, target, name, **options):
        """
        gets a unique file name in given target path.

        if the same file is already existed, it uses the digit slug generator
        to produce a slug and append it to the original requested name.

        :param str target: absolute target path to save the file.
        :param str name: file name to be used.

        :rtype: str
        """

        last_slug = None
        full_path = os.path.join(target, name)
        extension = path_utils.get_file_extension(full_path, remove_dot=False, lowercase=False)
        while os.path.exists(full_path) is True:
            name = path_utils.get_file_name(full_path, include_extension=False)
            if last_slug is not None:
                name = name.rstrip(last_slug)

            last_slug = self._get_sequence_slug()
            name = '{name}{slug}{extension}'.format(name=name, slug=last_slug,
                                                    extension=extension)
            full_path = os.path.join(target, name)

        return name
