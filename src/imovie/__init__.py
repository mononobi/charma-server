# -*- coding: utf-8 -*-
"""
imovie package.
"""

from pyrin.application.base import Application


__version__ = '0.1'


class IMovieApplication(Application):
    """
    server should create an instance of this class on startup.
    """

    def get_application_version(self):
        """
        gets application version.

        this method must be overridden in subclasses.

        :raises CoreNotImplementedError: core not implemented error.

        :rtype: str
        """

        return __version__
