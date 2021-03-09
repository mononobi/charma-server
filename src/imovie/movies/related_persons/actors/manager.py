# -*- coding: utf-8 -*-
"""
movies related actors manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

from imovie.movies.models import Movie2ActorEntity
from imovie.movies.related_persons.actors import RelatedActorsPackage
from imovie.movies.related_persons.actors.exceptions import Movie2ActorDoesNotExistError


class RelatedActorsManager(Manager):
    """
    movies related actors manager class.
    """

    package_class = RelatedActorsPackage

    NAME_NORMALIZERS = [NormalizerEnum.PERSIAN_SIGN,
                        NormalizerEnum.LATIN_SIGN,
                        NormalizerEnum.PERSIAN_NUMBER,
                        NormalizerEnum.ARABIC_NUMBER,
                        NormalizerEnum.PERSIAN_LETTER,
                        NormalizerEnum.LATIN_LETTER,
                        NormalizerEnum.LOWERCASE,
                        NormalizerEnum.SPACE]

    def _get(self, movie_id, person_id):
        """
        gets movie to actor with given ids.

        it returns None if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :rtype: Movie2ActorEntity
        """

        store = get_current_store()
        return store.query(Movie2ActorEntity).get((movie_id, person_id))

    def _get_normalized(self, value):
        """
        gets normalized value from given value.

        :param str value: value to be normalized.

        :rtype: str
        """

        return normalizer_services.normalize(value, *self.NAME_NORMALIZERS)

    def get(self, movie_id, person_id):
        """
        gets movie to actor with given ids.

        it raises an error if it does not exist.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :raises Movie2ActorDoesNotExistError: movie 2 actor does not exist error.

        :rtype: Movie2ActorEntity
        """

        entity = self._get(movie_id, person_id)
        if entity is None:
            raise Movie2ActorDoesNotExistError(_('Movie to actor with movie id [{movie}] '
                                                 'and actor id [{person}] does not exist.')
                                               .format(movie=movie_id, person=person_id))
        return entity

    def create(self, movie_id, person_id, **options):
        """
        creates a new movie 2 actor record.

        :param uuid.UUID movie_id: movie id.
        :param uuid.UUID person_id: person id.

        :keyword bool is_star: is star.
        :keyword str character: character name.
        """

        options.update(movie_id=movie_id, person_id=person_id)
        validator_services.validate_dict(Movie2ActorEntity, options)
        entity = Movie2ActorEntity(**options)
        entity.movie_id = movie_id
        entity.person_id = person_id
        entity.search_character = self._get_normalized(entity.character)
        entity.save()
