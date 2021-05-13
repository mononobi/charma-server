# -*- coding: utf-8 -*-
"""
updater processors language module.
"""

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class LanguageProcessor(ProcessorBase):
    """
    language processor class.
    """

    _category = UpdaterCategoryEnum.LANGUAGE

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param list[str] data: list of languages to be processed.
        """
        pass
