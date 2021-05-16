# -*- coding: utf-8 -*-
"""
updater services module.
"""

from pyrin.application.services import get_component

from imovie.updater import UpdaterPackage


def register_updater(instance, **options):
    """
    registers a new updater.

    :param AbstractUpdater instance: updater to be registered.
                                     it must be an instance of
                                     AbstractUpdater.

    :raises InvalidUpdaterTypeError: invalid updater type error.
    :raises DuplicateUpdaterError: duplicate updater error.
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).register_updater(instance, **options)


def register_processor(instance, **options):
    """
    registers a new processor.

    :param AbstractProcessor instance: processor to be registered.
                                       it must be an instance of
                                       AbstractProcessor.

    :raises InvalidProcessorTypeError: invalid processor type error.
    :raises DuplicateProcessorError: duplicate processor error.
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).register_processor(instance, **options)


def get_updater(category, **options):
    """
    gets the first element of chained updaters for given category.

    :param str category: category name.

    :raises UpdaterCategoryNotFoundError: updater category not found error.

    :rtype: AbstractUpdater
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).get_updater(category, **options)


def get_processor(category, **options):
    """
    gets the update processor for given category.

    :param str category: category name.

    :raises ProcessorCategoryNotFoundError: processor category not found error.

    :rtype: AbstractProcessor
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).get_processor(category, **options)


def try_get_processor(category, **options):
    """
    gets the update processor for given category.

    it returns None if no processor found.

    :param str category: category name.

    :rtype: AbstractProcessor
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).try_get_processor(category, **options)


def fetch(url, category, **options):
    """
    fetches data from given url for given category.

    it may return None if no data is available.

    :param str url: url to fetch data from it.
    :param str category: category of updaters to be used.

    :keyword bs4.BeautifulSoup content: the html content of input url.

    :raises UpdaterCategoryNotFoundError: updater category not found error.

    :returns: dict[str category, object value]
    :rtype: dict
    """

    return get_component(UpdaterPackage.COMPONENT_NAME).fetch(url, category, **options)


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

    return get_component(UpdaterPackage.COMPONENT_NAME).fetch_all(url, *categories, **options)


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

    return get_component(UpdaterPackage.COMPONENT_NAME).update(movie_id, **options)


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

    return get_component(UpdaterPackage.COMPONENT_NAME).update_all(**options)
