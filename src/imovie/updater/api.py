# -*- coding: utf-8 -*-
"""
updater api module.
"""

from pyrin.api.router.decorators import api
from pyrin.core.enumerations import HTTPMethodEnum

import imovie.updater.services as updater_services


@api('/updater/fetch_all', authenticated=False)
def fetch_all(url, *categories, **options):
    """
    fetches data from given url for specified categories.

    :param str url: url to fetch data from it.

    :param str categories: categories of updaters to be used.
                           if not provided, all categories will be used.

    :raises UpdaterCategoryNotFoundError: updater category not found error.

    :returns: a dict of all updated values and their categories.
    :rtype: dict
    """

    return updater_services.fetch_all(url, *categories, **options)


@api('/updater/<uuid:movie_id>', methods=HTTPMethodEnum.PATCH, authenticated=False)
def update(movie_id, **options):
    """
    updates the info of given movie.

    it returns a value indicating that update is done.

    :param uuid.UUID movie_id: movie id.

    :keyword bool content_rate: update content rate.
                                defaults to True if not provided.

    :keyword bool country: update country.
                           defaults to True if not provided.

    :keyword bool genre: update genre.
                         defaults to True if not provided.

    :keyword bool imdb_rate: update imdb rate.
                             defaults to True if not provided.

    :keyword bool language: update language.
                            defaults to True if not provided.

    :keyword bool meta_score: update meta score.
                              defaults to True if not provided.

    :keyword bool movie_poster: update movie poster.
                                defaults to True if not provided.

    :keyword bool original_title: update original title.
                                  defaults to True if not provided.

    :keyword bool production_year: update production year.
                                   defaults to True if not provided.

    :keyword bool runtime: update runtime.
                           defaults to True if not provided.

    :keyword bool storyline: update storyline.
                             defaults to True if not provided.

    :keyword bool title: update title.
                         defaults to True if not provided.

    :keyword str imdb_page: an imdb movie page to be used to fetch data from.
                            if not provided the movie page will be fetched
                            automatically if possible.

    :keyword bool force: force update data even if a category already
                         has valid data. defaults to False if not provided.

    :raises ValidationError: validation error.
    :raises MovieIMDBPageNotFoundError: movie imdb page not found error.

    :rtype: bool
    """

    return updater_services.update(movie_id, **options)


@api('/updater/update_all', methods=HTTPMethodEnum.PATCH, authenticated=False)
def update_all(**options):
    """
    updates the info of all movies.

    :keyword datetime from_created_on: update movies added from this datetime.
    :keyword datetime to_created_on: update movies added to this datetime.

    :keyword bool content_rate: update content rate.
                                defaults to True if not provided.

    :keyword bool country: update country.
                           defaults to True if not provided.

    :keyword bool genre: update genre.
                         defaults to True if not provided.

    :keyword bool imdb_rate: update imdb rate.
                             defaults to True if not provided.

    :keyword bool language: update language.
                            defaults to True if not provided.

    :keyword bool meta_score: update meta score.
                              defaults to True if not provided.

    :keyword bool movie_poster: update movie poster.
                                defaults to True if not provided.

    :keyword bool original_title: update original title.
                                  defaults to True if not provided.

    :keyword bool production_year: update production year.
                                   defaults to True if not provided.

    :keyword bool runtime: update runtime.
                           defaults to True if not provided.

    :keyword bool storyline: update storyline.
                             defaults to True if not provided.

    :keyword bool title: update title.
                         defaults to True if not provided.

    :keyword bool force: force update data even if a category already
                         has valid data. defaults to False if not provided.

    :returns: dict(total: total processed movies count,
                   updated: updated movies count,
                   not_updated: not updated movies count,
                   failed: failed to update movies count)
    :rtype: dict
    """

    return updater_services.update_all(**options)
