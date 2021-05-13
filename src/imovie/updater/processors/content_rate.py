# -*- coding: utf-8 -*-
"""
updater processors content rate module.
"""

import imovie.movies.content_rate.services as content_rate_services

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase


@processor()
class ContentRateProcessor(ProcessorBase):
    """
    content rate processor class.
    """

    _category = UpdaterCategoryEnum.CONTENT_RATE

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param str data: content rate to be processed.

        :returns: dict(uuid.UUID content_rate_id: content rate id)
        :rtype: dict
        """

        content_rate_id = None
        entity = content_rate_services.get_by_name(data)
        if entity is None:
            content_rate_id = content_rate_services.create(data)
        else:
            content_rate_id = entity.id

        return dict(content_rate_id=content_rate_id)
