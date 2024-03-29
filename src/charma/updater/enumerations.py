# -*- coding: utf-8 -*-
"""
updater enumerations module.
"""

from pyrin.core.decorators import class_property
from pyrin.core.enumerations import CoreEnum


class UpdaterCategoryEnum(CoreEnum):
    """
    updater category enum.
    """

    CONTENT_RATE = 'content_rate'
    COUNTRY = 'country'
    GENRE = 'genre'
    LANGUAGE = 'language'
    META_SCORE = 'meta_score'
    POSTER_NAME = 'poster_name'
    ORIGINAL_TITLE = 'original_title'
    PRODUCTION_YEAR = 'production_year'
    IMDB_RATE = 'imdb_rate'
    RUNTIME = 'runtime'
    STORYLINE = 'storyline'
    TITLE = 'title'
    ACTORS = 'actors'
    DIRECTORS = 'directors'

    @class_property
    def persons(self):
        """
        gets all enumeration values related to persons.

        :rtype: tuple[str]
        """

        return self.ACTORS, self.DIRECTORS
