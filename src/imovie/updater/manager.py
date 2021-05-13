# -*- coding: utf-8 -*-
"""
updater manager module.
"""

from collections import OrderedDict

import pyrin.validator.services as validator_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager, Context
from pyrin.logging.contexts import suppress

import imovie.scraper.services as scraper_services
import imovie.movies.services as movie_services
import imovie.search.services as search_services

from imovie.movies.models import MovieEntity
from imovie.updater import UpdaterPackage
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.search.enumerations import SearchCategoryEnum
from imovie.updater.interface import AbstractUpdater, AbstractProcessor
from imovie.updater.exceptions import InvalidUpdaterTypeError, DuplicateUpdaterError, \
    UpdaterCategoryNotFoundError, MovieIMDBPageNotFoundError, InvalidProcessorTypeError, \
    DuplicateProcessorError, ProcessorCategoryNotFoundError


class UpdaterManager(Manager):
    """
    updater manager class.
    """

    package_class = UpdaterPackage

    def __init__(self):
        """
        initializes an instance of UpdaterManager.
        """

        super().__init__()

        # a dict containing all updater handlers for each category. in the form of:
        # {str category: {str name: AbstractUpdater updater}}
        self._updaters = Context()

        # a dict containing update processors for each category. in the form of:
        # {str category: AbstractProcessor processor}
        self._processors = Context()

    def _get_updaters(self, category, **options):
        """
        gets a dict of all updaters of given category.

        :param str category: category name.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :rtype: dict[str, AbstractUpdater]
        """

        if category not in self._updaters:
            raise UpdaterCategoryNotFoundError('Updater category [{category}] not '
                                               'found.'.format(category=category))

        return self._updaters.get(category)

    def _set_next_handlers(self, updaters):
        """
        sets next handler for each updater in the input list.

        :param dict[str, AbstractUpdater] updaters: dict of updaters.
        """

        instances = list(updaters.values())
        length = len(updaters)
        for i in range(length):
            if i == length - 1:
                instances[i].set_next(None)
            else:
                instances[i].set_next(instances[i + 1])

    def register_updater(self, instance, **options):
        """
        registers a new updater.

        :param AbstractUpdater instance: updater to be registered.
                                         it must be an instance of
                                         AbstractUpdater.

        :raises InvalidUpdaterTypeError: invalid updater type error.
        :raises DuplicateUpdaterError: duplicate updater error.
        """

        if not isinstance(instance, AbstractUpdater):
            raise InvalidUpdaterTypeError('Input parameter [{instance}] is '
                                          'not an instance of [{base}].'
                                          .format(instance=instance,
                                                  base=AbstractUpdater))

        previous_instances = self._updaters.get(instance.category, OrderedDict())
        if instance.category in self._updaters and instance.name in previous_instances:
            raise DuplicateUpdaterError('There is another registered updater with '
                                        'name [{name}] and category [{category}].'
                                        .format(name=instance.name,
                                                category=instance.category))

        previous_instances[instance.name] = instance
        self._set_next_handlers(previous_instances)
        self._updaters[instance.category] = previous_instances

    def register_processor(self, instance, **options):
        """
        registers a new processor.

        :param AbstractProcessor instance: processor to be registered.
                                           it must be an instance of
                                           AbstractProcessor.

        :raises InvalidProcessorTypeError: invalid processor type error.
        :raises DuplicateProcessorError: duplicate processor error.
        """

        if not isinstance(instance, AbstractProcessor):
            raise InvalidProcessorTypeError('Input parameter [{instance}] is '
                                            'not an instance of [{base}].'
                                            .format(instance=instance,
                                                    base=AbstractProcessor))

        if instance.category in self._processors:
            raise DuplicateProcessorError('There is another registered update '
                                          'processor for category [{category}].'
                                          .format(name=instance.name,
                                                  category=instance.category))

        self._processors[instance.category] = instance

    def get_updater(self, category, **options):
        """
        gets the first element of chained updaters for given category.

        :param str category: category name.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :rtype: AbstractUpdater
        """

        updaters = self._get_updaters(category, **options)
        updaters = list(updaters.values())
        return updaters[0]

    def get_processor(self, category, **options):
        """
        gets the update processor for given category.

        :param str category: category name.

        :raises ProcessorCategoryNotFoundError: processor category not found error.

        :rtype: AbstractProcessor
        """

        if category not in self._processors:
            raise ProcessorCategoryNotFoundError('Processor category [{category}] not '
                                                 'found.'.format(category=category))

        return self._processors.get(category)

    def try_get_processor(self, category, **options):
        """
        gets the update processor for given category.

        it returns None if no processor found.

        :param str category: category name.

        :rtype: AbstractProcessor
        """

        with suppress(ProcessorCategoryNotFoundError, log=False):
            return self.get_processor(category, **options)

        return None

    def fetch(self, url, category, **options):
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

        updater = self.get_updater(category, **options)
        result = updater.fetch(url, **options)
        if result is None:
            return None

        final_result = dict()
        final_result[updater.category] = result
        return final_result

    def fetch_all(self, url, *categories, **options):
        """
        fetches data from given url for specified categories.

        :param str url: url to fetch data from it.

        :param str categories: categories of updaters to be used.
                               if not provided, all categories will be used.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :returns: a dict of all updated values and their categories.
        :rtype: dict
        """

        content = scraper_services.get(url, **options)
        options.update(content=content)
        categories = set(categories)
        if len(categories) <= 0:
            categories = UpdaterCategoryEnum.values()

        final_result = dict()
        for item in categories:
            result = self.fetch(url, item, **options)
            if result is not None:
                final_result.update(result)

        return final_result

    def update(self, movie_id, **options):
        """
        updates the info of given movie.

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
        """

        content_rate = options.get('content_rate', True)
        country = options.get('country', True)
        genre = options.get('genre', True)
        imdb_rate = options.get('imdb_rate', True)
        language = options.get('language', True)
        meta_score = options.get('meta_score', True)
        movie_poster = options.get('movie_poster', True)
        original_title = options.get('original_title', True)
        production_year = options.get('production_year', True)
        runtime = options.get('runtime', True)
        storyline = options.get('storyline', True)
        title = options.get('title', True)
        force = options.get('force', False)
        imdb_page = options.get('imdb_page')

        movie_id = validator_services.validate_field(MovieEntity, MovieEntity.id,
                                                     movie_id, nullable=False)

        entity = movie_services.get(movie_id)
        imdb_page = imdb_page or entity.imdb_page
        full_title = movie_services.get_full_title(entity.title or entity.library_title,
                                                   entity.production_year)
        if imdb_page in (None, ''):
            imdb_page = search_services.search(full_title, SearchCategoryEnum.MOVIE)
        else:
            validator_services.validate_field(MovieEntity, MovieEntity.imdb_page,
                                              imdb_page, nullable=False)

        if imdb_page is None:
            raise MovieIMDBPageNotFoundError(_('IMDb page for movie [{title}] could '
                                               'not be found.').format(name=full_title))

        categories = []
        if content_rate is True and (force is True or entity.content_rate_id is None):
            categories.append(UpdaterCategoryEnum.CONTENT_RATE)

        if country is True:
            categories.append(UpdaterCategoryEnum.COUNTRY)

        if genre is True:
            categories.append(UpdaterCategoryEnum.GENRE)

        if imdb_rate is True and (force is True or entity.imdb_rate is None):
            categories.append(UpdaterCategoryEnum.IMDB_RATE)

        if language is True:
            categories.append(UpdaterCategoryEnum.LANGUAGE)

        if meta_score is True and (force is True or entity.meta_score is None):
            categories.append(UpdaterCategoryEnum.META_SCORE)

        if movie_poster is True and (force is True or entity.poster_name is None):
            categories.append(UpdaterCategoryEnum.POSTER_NAME)

        if original_title is True and (force is True or entity.original_title is None):
            categories.append(UpdaterCategoryEnum.ORIGINAL_TITLE)

        if production_year is True and (force is True or entity.production_year is None):
            categories.append(UpdaterCategoryEnum.PRODUCTION_YEAR)

        if runtime is True and (force is True or entity.runtime is None):
            categories.append(UpdaterCategoryEnum.RUNTIME)

        if storyline is True and (force is True or entity.storyline is None):
            categories.append(UpdaterCategoryEnum.STORYLINE)

        if title is True and (force is True or entity.title is None):
            categories.append(UpdaterCategoryEnum.TITLE)

        updated_fields = dict()
        if len(categories) > 0:
            updated_fields = self.fetch_all(imdb_page, *categories)

        updated_fields.update(imdb_page=imdb_page)
        movie_services.update(entity.id, **updated_fields)
        return updated_fields
