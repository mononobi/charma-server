# -*- coding: utf-8 -*-
"""
updater processors country module.
"""

import imovie.countries.services as country_services
import imovie.movies.related_countries.services as related_country_services

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

        :keyword str imdb_page: movie imdb page.
        """

        related_country_services.delete_by_movie(movie_id, **options)
        for index, item in enumerate(data):
            is_main = index == 0
            country = country_services.get_by_name(item)
            country_id = None
            if country is not None:
                country_id = country.id
            else:
                country_id = country_services.create(item, **options)

            related_country_services.create(movie_id, country_id, is_main=is_main)
