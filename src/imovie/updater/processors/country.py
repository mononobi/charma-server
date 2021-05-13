# -*- coding: utf-8 -*-
"""
updater processors country module.
"""

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class CountryProcessor(ProcessorBase):
    """
    country processor class.
    """

    _category = UpdaterCategoryEnum.COUNTRY

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param list[str] data: list of countries to be processed.
        """
        pass
