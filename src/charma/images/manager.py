# -*- coding: utf-8 -*-
"""
images manager module.
"""

import os

from abc import abstractmethod

import pyrin.utils.path as path_utils

from pyrin.core.structs import Manager
from pyrin.core.exceptions import CoreNotImplementedError

from charma.images import ImagesPackage


class ImagesManager(Manager):
    """
    images manager class.

    this is the base class for all image managers.
    """

    package_class = ImagesPackage

    def __init__(self):
        """
        initializes an instance of ImagesManager.
        """

        super().__init__()

        self._root_directory = self._get_root_directory()
        self._create_root_directory()

    def _create_root_directory(self):
        """
        creates images root directory.
        """

        path_utils.create_directory(self._root_directory, ignore_existed=True)

    @abstractmethod
    def _get_root_directory(self):
        """
        gets the root directory for images.

        this method is intended to be overridden in subclasses.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        raise CoreNotImplementedError()

    def _delete(self, name):
        """
        deletes an image with given name.

        :param str name: image name to be deleted.
        """

        full_path = self.get_full_path(name)
        if path_utils.exists(full_path):
            path_utils.remove_file(full_path)

    def get_root_directory(self):
        """
        gets the root directory for images.

        :rtype: str
        """

        return self._root_directory

    def get_full_path(self, name):
        """
        gets the full path of image with given name.

        :param str name: image name.

        :rtype: str
        """

        return os.path.join(self._root_directory, name)

    def exists(self, name):
        """
        gets a value indicating that an image with given name exists.

        :param str name: image name.

        :rtype: bool
        """

        full_path = self.get_full_path(name)
        return path_utils.exists(full_path)
