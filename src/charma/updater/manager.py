# -*- coding: utf-8 -*-
"""
updater manager module.
"""

from collections import OrderedDict
from datetime import timedelta

import pyrin.validator.services as validator_services
import pyrin.logging.services as logging_services
import pyrin.configuration.services as config_services
import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager, Context
from pyrin.database.services import get_current_store
from pyrin.logging.contexts import suppress
from pyrin.database.transaction.contexts import atomic_context

import charma.scraper.services as scraper_services
import charma.movies.services as movie_services
import charma.search.services as search_services
import charma.movies.related_languages.services as related_language_services
import charma.movies.related_genres.services as related_genre_services
import charma.movies.related_countries.services as related_country_services
import charma.movies.related_persons.actors.services as related_actor_services
import charma.movies.related_persons.directors.services as related_director_services

from charma.movies.models import MovieEntity
from charma.updater import UpdaterPackage
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.search.enumerations import SearchCategoryEnum
from charma.updater.interface import AbstractUpdater, AbstractProcessor
from charma.updater.exceptions import InvalidUpdaterTypeError, DuplicateUpdaterError, \
    UpdaterCategoryNotFoundError, MovieIMDBPageNotFoundError, InvalidProcessorTypeError, \
    DuplicateProcessorError, ProcessorCategoryNotFoundError


class UpdaterManager(Manager):
    """
    updater manager class.
    """

    package_class = UpdaterPackage
    LOGGER = logging_services.get_logger('updater')
    CREDITS_URL_PATTERN = '{base}/fullcredits'

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

    def _process(self, movie_id, data, **options):
        """
        processes given data using related processors and returns the processed data.

        :param uuid.UUID movie_id: movie id.
        :param dict data: data to be processed.

        :keyword str imdb_page: movie imdb page.

        :rtype: dict
        """

        processed_result = dict()
        for category, value in data.items():
            processor = self.try_get_processor(category)
            if processor is None:
                processed_result[category] = value
            else:
                result = processor.process(movie_id, value, **options)
                if result is not None:
                    processed_result.update(result)

        return processed_result

    def _needs_update(self, current_value, force, modified_time):
        """
        gets a value indicating that a field must be updated.

        :param object current_value: current value of the field.
        :param bool force: force update is required.
        :param datetime.datetime modified_time: last modified time.

        :rtype: bool
        """

        if force is True:
            return True

        if current_value is not None:
            return False

        if modified_time is None:
            return True

        interval = config_services.get('updater', 'general', 'update_interval')
        now = datetime_services.now()
        next_interval = modified_time + timedelta(days=interval)
        return now >= next_interval

    def _get_max_modified_on(self):
        """
        gets the maximum modified on value to select movies to this value for update.

        :rtype: datetime.datetime
        """

        interval = config_services.get('updater', 'general', 'update_interval')
        now = datetime_services.now()
        return now - timedelta(days=interval)

    def _get_credits_url(self, url):
        """
        gets credits url for given imdb page url.

        :param str url: imdb page url.

        :rtype: str
        """

        return self.CREDITS_URL_PATTERN.format(base=url)

    def _fetch(self, content, category, **options):
        """
        fetches data from given content for given category.

        it may return None if no data is available.

        :param bs4.BeautifulSoup content: the html content of imdb page.
        :param str category: category of updaters to be used.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :returns: dict[str category, object value]
        :rtype: dict
        """

        updater = self.get_updater(category, **options)
        result = updater.fetch(content, **options)
        if result is None:
            return None

        final_result = dict()
        final_result[updater.category] = result
        return final_result

    def _fetch_all(self, url, *categories, **options):
        """
        fetches data from given url for specified categories.

        :param str url: url to fetch data from it.

        :param str categories: categories of updaters to be used.
                               if not provided, all categories will be used.

        :raises UpdaterCategoryNotFoundError: updater category not found error.

        :returns: a dict of all updated values and their categories.
        :rtype: dict
        """

        content = scraper_services.get_soup(url, **options)
        categories = set(categories)
        if len(categories) <= 0:
            categories = UpdaterCategoryEnum.values()

        person_categories = set(UpdaterCategoryEnum.persons).intersection(set(categories))
        if len(person_categories) > 0:
            with suppress():
                credits_url = self._get_credits_url(url)
                credits_content = scraper_services.get_soup(credits_url, **options)
                options.update(credits=credits_content)

        final_result = dict()
        for item in categories:
            result = self._fetch(content, item, **options)
            if result is not None:
                final_result.update(result)

        return final_result

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

    def update(self, movie_id, **options):
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

        :keyword bool actors: update actors.
                              defaults to True if not provided.

        :keyword bool directors: update directors.
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
        actors = options.get('actors', True)
        directors = options.get('directors', True)
        force = options.get('force', False)
        imdb_page = options.get('imdb_page')

        movie_id = validator_services.validate_field(MovieEntity, MovieEntity.id,
                                                     movie_id, nullable=False)

        entity = movie_services.get(movie_id)
        imdb_page = imdb_page or entity.imdb_page
        full_title = movie_services.get_full_title(entity.title or entity.library_title,
                                                   entity.production_year)

        if imdb_page is None and \
                self._needs_update(imdb_page, force, entity.modified_on) is True:
            imdb_page = search_services.search(full_title, SearchCategoryEnum.MOVIE)

        if imdb_page is None:
            # we update 'imdb_page' to refresh 'modified_on' value.
            store = get_current_store()
            entity.update(imdb_page=imdb_page)
            store.commit()
            raise MovieIMDBPageNotFoundError(_('IMDb page for movie [{title}] could '
                                               'not be found.').format(title=full_title))
        else:
            validator_services.validate_field(MovieEntity, MovieEntity.imdb_page,
                                              imdb_page, nullable=False)

        categories = []
        if content_rate is True and self._needs_update(entity.content_rate_id,
                                                       force, entity.modified_on):
            categories.append(UpdaterCategoryEnum.CONTENT_RATE)

        has_country = related_country_services.exists(movie_id) or None
        if country is True and self._needs_update(has_country, force,
                                                  entity.modified_on):
            categories.append(UpdaterCategoryEnum.COUNTRY)

        has_genre = related_genre_services.exists(movie_id) or None
        if genre is True and self._needs_update(has_genre, force,
                                                entity.modified_on):
            categories.append(UpdaterCategoryEnum.GENRE)

        if imdb_rate is True and self._needs_update(entity.imdb_rate, force,
                                                    entity.modified_on):
            categories.append(UpdaterCategoryEnum.IMDB_RATE)

        has_language = related_language_services.exists(movie_id) or None
        if language is True and self._needs_update(has_language, force,
                                                   entity.modified_on):
            categories.append(UpdaterCategoryEnum.LANGUAGE)

        if meta_score is True and self._needs_update(entity.meta_score, force,
                                                     entity.modified_on):
            categories.append(UpdaterCategoryEnum.META_SCORE)

        if movie_poster is True and self._needs_update(entity.poster_name, force,
                                                       entity.modified_on):
            categories.append(UpdaterCategoryEnum.POSTER_NAME)

        if original_title is True and self._needs_update(entity.original_title, force,
                                                         entity.modified_on):
            categories.append(UpdaterCategoryEnum.ORIGINAL_TITLE)

        if production_year is True and self._needs_update(entity.production_year, force,
                                                          entity.modified_on):
            categories.append(UpdaterCategoryEnum.PRODUCTION_YEAR)

        if runtime is True and self._needs_update(entity.runtime, force,
                                                  entity.modified_on):
            categories.append(UpdaterCategoryEnum.RUNTIME)

        if storyline is True and self._needs_update(entity.storyline, force,
                                                    entity.modified_on):
            categories.append(UpdaterCategoryEnum.STORYLINE)

        if title is True and self._needs_update(entity.title, force,
                                                entity.modified_on):
            categories.append(UpdaterCategoryEnum.TITLE)

        has_actor = related_actor_services.exists(movie_id) or None
        if actors is True and self._needs_update(has_actor, force,
                                                 entity.modified_on):
            categories.append(UpdaterCategoryEnum.ACTORS)

        has_director = related_director_services.exists(movie_id) or None
        if directors is True and self._needs_update(has_director, force,
                                                    entity.modified_on):
            categories.append(UpdaterCategoryEnum.DIRECTORS)

        # this code is to try to correct production year even if it has valid value.
        # because it is possible that the production year extracted from library
        # title be incorrect.
        if production_year is True and len(categories) > 0 \
                and UpdaterCategoryEnum.PRODUCTION_YEAR not in categories:
            categories.append(UpdaterCategoryEnum.PRODUCTION_YEAR)

        updated_fields = dict()
        if len(categories) > 0:
            updated_fields = self._fetch_all(imdb_page, *categories)
            options.update(imdb_page=imdb_page)
            updated_fields = self._process(entity.id, updated_fields, **options)

        if imdb_page != entity.imdb_page:
            updated_fields.update(imdb_page=imdb_page)

        if len(updated_fields) > 0:
            movie_services.update(entity.id, **updated_fields)
            return True

        return False

    def update_all(self, **options):
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

        :keyword bool actors: update actors.
                              defaults to True if not provided.

        :keyword bool directors: update directors.
                                 defaults to True if not provided.

        :keyword bool force: force update data even if a category already
                             has valid data. defaults to False if not provided.

        :returns: dict(total: total processed movies count,
                       updated: updated movies count,
                       not_updated: not updated movies count,
                       failed: failed to update movies count)
        :rtype: dict
        """

        force = options.get('force', False)
        from_created_on = options.pop('from_created_on', None)
        to_created_on = options.pop('to_created_on', None)
        modified_on_criteria = dict()
        if force is not True:
            to_modified_on = self._get_max_modified_on()
            modified_on_criteria.update(to_modified_on=to_modified_on)

        movies = movie_services.find(from_created_on=from_created_on,
                                     to_created_on=to_created_on,
                                     columns=[MovieEntity.id],
                                     order_by='-created_time',
                                     **modified_on_criteria)

        updated = 0
        not_updated = 0
        failed = 0
        for item in movies:
            try:
                with atomic_context():
                    result = self.update(item.id, **options)
                    if result is True:
                        updated += 1
                    else:
                        not_updated += 1
            except Exception as error:
                failed += 1
                self.LOGGER.exception(str(error))

        return dict(total=len(movies),
                    updated=updated,
                    not_updated=not_updated,
                    failed=failed)
