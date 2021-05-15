# -*- coding: utf-8 -*-
"""
updater processors language module.
"""

import imovie.languages.services as language_services
import imovie.movies.related_languages.services as related_language_services

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

        related_language_services.delete_by_movie(movie_id, **options)
        languages = []
        for item in data:
            language = language_services.get_by_name(item)
            language_id = None
            if language is not None:
                language_id = language.id
            else:
                language_id = language_services.create(item, **options)

            languages.append(language_id)

        for index, item in enumerate(languages):
            is_main = index == 0
            related_language_services.create(movie_id, item, is_main=is_main)
