# -*- coding: utf-8 -*-
"""
updater enumerations module.
"""

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

    # these two values have no relevant registered updater.
    # they will be injected into each updater through options.
    ACTORS_PHOTO = 'actors_photo'
    DIRECTORS_PHOTO = 'directors_photo'

    @property
    def persons(self):
        """
        gets all enumeration values related to persons.

        :rtype: tuple[str]
        """

        return self.ACTORS, self.ACTORS_PHOTO, self.DIRECTORS, self.DIRECTORS_PHOTO
