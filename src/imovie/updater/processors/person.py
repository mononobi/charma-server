# -*- coding: utf-8 -*-
"""
updater processors person module.
"""

from abc import abstractmethod

import pyrin.utilities.string.normalizer.services as normalizer_services
import pyrin.utils.path as path_utils

from pyrin.logging.contexts import suppress
from pyrin.core.exceptions import CoreNotImplementedError

import imovie.persons.services as person_services
import imovie.persons.images.services as person_image_services
import imovie.movies.related_persons.actors.services as related_actor_services
import imovie.movies.related_persons.directors.services as related_director_services
import imovie.downloader.services as downloader_services

from imovie.updater.decorators import processor
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.processors.base import ProcessorBase
from imovie.persons.enumerations import PersonTypeEnum


class PersonProcessorBase(ProcessorBase):
    """
    person processor class.
    """

    # type of this person.
    # it must be set to a value from 'PersonTypeEnum'.
    _type = None

    def _download_photo(self, imdb_page, photo_url):
        """
        downloads the photo of given person if it does not exist.

        it returns the downloaded photo name or None.
        it ignores downloading if photo is already existed or photo url is None.

        :param str imdb_page: person imdb page.
        :param str photo_url: photo url to be downloaded.
        """

        if photo_url is None or imdb_page in (None, ''):
            return None

        imdb_page = normalizer_services.normalize(imdb_page)
        extension = path_utils.get_file_extension(photo_url, remove_dot=False, lowercase=False)
        file_name = '{name}{extension}'.format(name=imdb_page, extension=extension)

        if person_image_services.exists(file_name) is True:
            return file_name

        image_root = person_image_services.get_root_directory()
        with suppress():
            _, name = downloader_services.download(photo_url, image_root, name=imdb_page)
            return name

        return None

    @abstractmethod
    def _delete_related_persons(self, movie_id):
        """
        deletes all related persons to given movie.

        this method must be overridden in subclasses.

        :param uuid.UUID movie_id: movie id to delete all related persons of it.

        :raises CoreNotImplementedError: core not implemented error.
        """

        raise CoreNotImplementedError()

    @abstractmethod
    def _create_related_person(self, movie_id, person_id, **options):
        """
        creates a related person to given movie.

        this method must be overridden in subclasses.

        :param uuid.UUID movie_id: movie id to relate person to it.
        :param uuid.UUID person_id: person id to be related to movie.

        :raises CoreNotImplementedError: core not implemented error.
        """

        raise CoreNotImplementedError()

    def process(self, movie_id, data, **options):
        """
        processes given update data.

        :param uuid.UUID movie_id: movie id to process data for it.
        :param list[dict] data: list of persons to be processed.

        :keyword str imdb_page: movie imdb page.
        """

        self._delete_related_persons(movie_id)
        for item in data:
            person = person_services.try_get(**item)
            person_id = None
            if person is not None:
                person_id = person.id
            else:
                fullname = item.pop('fullname', None)
                photo_name = self._download_photo(item.get('imdb_page'), item.get('photo_name'))
                item.update(type=self._type, photo_name=photo_name)
                person_id = person_services.create(fullname, **item)

            self._create_related_person(movie_id, person_id, **item)


@processor()
class ActorProcessor(PersonProcessorBase):
    """
    actor processor class.
    """

    _type = PersonTypeEnum.ACTOR
    _category = UpdaterCategoryEnum.ACTORS

    def _delete_related_persons(self, movie_id):
        """
        deletes all related actors to given movie.

        :param uuid.UUID movie_id: movie id to delete all related actors of it.
        """

        related_actor_services.delete_by_movie(movie_id)

    def _create_related_person(self, movie_id, person_id, **options):
        """
        creates a related actor to given movie.

        :param uuid.UUID movie_id: movie id to relate actor to it.
        :param uuid.UUID person_id: actor id to be related to movie.
        """

        related_actor_services.create(movie_id, person_id, **options)


@processor()
class DirectorProcessor(PersonProcessorBase):
    """
    director processor class.
    """

    _type = PersonTypeEnum.DIRECTOR
    _category = UpdaterCategoryEnum.DIRECTORS

    def _delete_related_persons(self, movie_id):
        """
        deletes all related directors to given movie.

        :param uuid.UUID movie_id: movie id to delete all related directors of it.
        """

        related_director_services.delete_by_movie(movie_id)

    def _create_related_person(self, movie_id, person_id, **options):
        """
        creates a related director to given movie.

        :param uuid.UUID movie_id: movie id to relate director to it.
        :param uuid.UUID person_id: director id to be related to movie.
        """

        related_director_services.create(movie_id, person_id, **options)
