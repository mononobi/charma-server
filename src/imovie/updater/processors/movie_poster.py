# -*- coding: utf-8 -*-
"""
updater processors movie poster module.
"""

from pyrin.logging.contexts import suppress

import imovie.movies.services as movie_services
import imovie.movies.images.services as movie_image_services
import imovie.downloader.services as downloader_services

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class MoviePosterProcessor(ProcessorBase):
    """
    movie poster processor class.
    """

    _category = UpdaterCategoryEnum.POSTER_NAME

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        it returns None if poster downloading fails.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param str data: poster url to be processed.

        :returns: dict(str poster_name: poster name)
        :rtype: dict
        """

        title = movie_services.get_full_name_for_path(movie_id)
        image_root = movie_image_services.get_root_directory()

        with suppress():
            _, name = downloader_services.download(data, image_root, name=title)
            return dict(poster_name=name)

        return None
