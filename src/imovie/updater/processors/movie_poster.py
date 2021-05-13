# -*- coding: utf-8 -*-
"""
updater processors movie poster module.
"""

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
        pass
