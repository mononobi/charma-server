# -*- coding: utf-8 -*-
"""
updater processors movie poster module.
"""

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

        :param uuid.UUID movie_id: movie id to process data for it.
        :param str data: poster url to be processed.
        """

        title = movie_services.get_full_name_for_path(movie_id)
        image_root = movie_image_services.get_root_directory()
        _, name = downloader_services.download(data, image_root, name=title)
        return dict(poster_name=name)
