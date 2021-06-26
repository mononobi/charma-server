# -*- coding: utf-8 -*-
"""
updater processors movie poster module.
"""

import pyrin.utilities.string.normalizer.services as normalizer_services
import pyrin.utils.path as path_utils

from pyrin.logging.contexts import suppress

import charma.movies.images.services as movie_image_services
import charma.downloader.services as downloader_services

from charma.updater.decorators import processor
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.processors.base import ProcessorBase


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
        extension = path_utils.get_file_extension(data, remove_dot=False, lowercase=False)
        file_name = '{name}{extension}'.format(name=imdb_page, extension=extension)

        if movie_image_services.exists(file_name) is True:
            return dict(poster_name=file_name)

        image_root = movie_image_services.get_root_directory()
        with suppress():
            _, name = downloader_services.download(data, image_root, name=imdb_page)
            return dict(poster_name=name)

        return None
