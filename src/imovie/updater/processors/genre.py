# -*- coding: utf-8 -*-
"""
updater processors genre module.
"""

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class GenreProcessor(ProcessorBase):
    """
    genre processor class.
    """

    _category = UpdaterCategoryEnum.GENRE

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param list[str] data: list of genres to be processed.
        """
        pass
