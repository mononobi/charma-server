# -*- coding: utf-8 -*-
"""
updater processors movie poster module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.logging.contexts import suppress

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

        :keyword str imdb_page: movie imdb page.

        :returns: dict(str poster_name: poster name)
        :rtype: dict
        """

        imdb_page = self._get_imdb_page(**options)
        imdb_page = normalizer_services.normalize(imdb_page)
        image_root = movie_image_services.get_root_directory()

        with suppress():
            _, name = downloader_services.download(data, image_root, name=imdb_page)
            return dict(poster_name=name)

        return None
