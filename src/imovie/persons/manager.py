# -*- coding: utf-8 -*-
"""
persons manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.utilities.string.normalizer.services as normalizer_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager, Context
from pyrin.database.services import get_current_store
from pyrin.utils.sqlalchemy import add_datetime_range_clause
from pyrin.utilities.string.normalizer.enumerations import NormalizerEnum

from imovie.persons import PersonsPackage
from imovie.persons.handler import AbstractPersonHandler
from imovie.persons.models import PersonEntity
from imovie.persons.exceptions import PersonDoesNotExistError, InvalidPersonHandlerTypeError, \
    PersonHandlerNameRequiredError, DuplicatedPersonHandlerError, PersonHandlerNotExistedError


class PersonsManager(Manager):
    """
    persons manager class.
    """

    package_class = PersonsPackage

    NAME_NORMALIZERS = [NormalizerEnum.PERSIAN_SIGN,
                        NormalizerEnum.LATIN_SIGN,
                        NormalizerEnum.PERSIAN_NUMBER,
                        NormalizerEnum.ARABIC_NUMBER,
                        NormalizerEnum.PERSIAN_LETTER,
                        NormalizerEnum.LATIN_LETTER,
                        NormalizerEnum.LOWERCASE,
                        NormalizerEnum.SPACE]

    def __init__(self):
        """
        initializes an instance of PersonsManager.
        """

        super().__init__()

        # a dict containing person handlers. in the form of:
        # {str name: AbstractPersonHandler instance}
        self._handlers = Context()

    def _get_handler(self, name):
        """
        gets the person handler with given name.

        :param str name: handler name to be get.

        :raises PersonHandlerNotExistedError: person handler not existed error.

        :rtype: AbstractPersonHandler
        """

        if name not in self._handlers:
            raise PersonHandlerNotExistedError('Person handler [{name}] does not exist.'
                                               .format(name=name))

        return self._handlers.get(name)

    def _make_find_expressions(self, expressions, **filters):
        """
        makes find expressions with given filters.

        :param list expressions: list of expressions to add
                                 new expressions into it.

        :keyword str first_name: first name.
        :keyword str last_name: last name
        :keyword str imdb_page: imdb page link
        :keyword str photo_name: photo file name.
        :keyword datetime from_add_date: from add date.
        :keyword datetime to_add_date: to add date.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to True if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to True if not provided.

        :rtype: list
        """

        first_name = filters.get('first_name')
        last_name = filters.get('last_name')
        imdb_page = filters.get('imdb_page')
        photo_name = filters.get('photo_name')
        from_add_date = filters.get('from_add_date')
        to_add_date = filters.get('to_add_date')

        if first_name is not None or last_name is not None:
            search_name = self._get_search_name(first_name, last_name)
            expressions.append(PersonEntity.search_name.icontains(search_name))

        if imdb_page is not None:
            expressions.append(PersonEntity.imdb_page.icontains(imdb_page))

        if photo_name is not None:
            expressions.append(PersonEntity.photo_name.icontains(photo_name))

        if from_add_date is not None or to_add_date is not None:
            add_datetime_range_clause(expressions, PersonEntity.add_date,
                                      from_add_date, to_add_date, **filters)

    def _get(self, id):
        """
        gets person with given id.

        it returns None if person does not exist.

        :param int id: person id.

        :rtype: PersonEntity
        """

        store = get_current_store()
        return store.query(PersonEntity).get(id)

    def _get_all(self, *expressions):
        """
        gets all persons using provided expressions.

        :param object expressions: expressions to be applied by filter.

        :rtype: list[PersonEntity]
        """

        store = get_current_store()
        return store.query(PersonEntity).filter(*expressions).all()

    def _get_search_name(self, first_name, last_name):
        """
        gets search name from given inputs.

        :param str first_name: first name.
        :param str last_name: last name.

        :rtype: str
        """

        fullname = self.get_fullname(first_name, last_name)
        return normalizer_services.normalize(fullname, *self.NAME_NORMALIZERS)

    def register_handler(self, instance, **options):
        """
        registers a person handler.

        :param AbstractPersonHandler instance: handler instance.

        :raises InvalidPersonHandlerTypeError: invalid person handler type error.
        :raises PersonHandlerNameRequiredError: person handler name required error.
        :raises DuplicatedPersonHandlerError: duplicated person handler error.
        """

        if not isinstance(instance, AbstractPersonHandler):
            raise InvalidPersonHandlerTypeError('Input parameter [{instance}] is '
                                                'not an instance of [{base}].'
                                                .format(instance=instance,
                                                        base=AbstractPersonHandler))

        if instance.name in (None, '') or instance.name.isspace():
            raise PersonHandlerNameRequiredError('Person handler name [{instance}] '
                                                 'must be provided.'
                                                 .format(instance=instance))

        if instance.name is self._handlers:
            raise DuplicatedPersonHandlerError('There is another registered person handler '
                                               'with name [{name}], so new handler '
                                               '[{instance}] could not be registered.'
                                               .format(name=instance.name, instance=instance))

        self._handlers[instance.name] = instance

    def get_fullname(self, first_name, last_name):
        """
        gets full name from given inputs.

        :param str first_name: first name.
        :param str last_name: last name.

        :rtype: str
        """

        has_first_name = first_name not in (None, '') and not first_name.isspace()
        has_last_name = last_name not in (None, '') and not last_name.isspace()

        if has_first_name is True and has_last_name is True:
            return '{first} {last}'.format(first=first_name, last=last_name)

        if has_first_name is True:
            return first_name

        if has_last_name is True:
            return last_name

        return ''

    def get(self, id):
        """
        gets person with given id.

        it raises an error if person does not exist.

        :param int id: person id.

        :raises PersonDoesNotExistError: person does not exist error.

        :rtype: PersonEntity
        """

        entity = self._get(id)
        if entity is None:
            raise PersonDoesNotExistError(_('Person with id [{id}] does not exist.')
                                          .format(id=id))
        return entity

    def create(self, first_name, **options):
        """
        creates a new person.

        :param str first_name: first name.

        :keyword str last_name: last name.
        :keyword str imdb_page: imdb page link.
        :keyword str photo_name: photo file name.

        :keyword str handler: person handler name to be used.
                              defaults to None if not provided.

        :raises ValidationError: validation error.

        :returns: created person id.
        :rtype: int
        """

        options.update(first_name=first_name)
        validator_services.validate_dict(PersonEntity, options)
        search_name = self._get_search_name(first_name, options.get('last_name'))
        entity = PersonEntity(**options)
        entity.search_name = search_name
        entity.identifier = entity.imdb_page
        entity.save(flush=True)

        handler_name = options.get('handler')
        if handler_name is not None:
            handler = self._get_handler(handler_name)
            handler.create(entity.id, **options)

        return entity.id

    def find(self, **filters):
        """
        finds persons with given filters.

        :keyword str first_name: first name.
        :keyword str last_name: last name
        :keyword str imdb_page: imdb page link
        :keyword str photo_name: photo file name.
        :keyword datetime from_add_date: from add date.
        :keyword datetime to_add_date: to add date.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to True if not provided.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to True if not provided.

        :rtype: list[PersonEntity]
        """

        expressions = []
        self._make_find_expressions(expressions, **filters)
        return self._get_all(*expressions)

    def exists(self, first_name, last_name):
        """
        gets a value indicating that a person with given first and last name exists.

        :param str first_name: first name.
        :param str last_name: last name

        :rtype: bool
        """

        search_name = self._get_search_name(first_name, last_name)
        store = get_current_store()
        return store.query(PersonEntity.id).filter(
            PersonEntity.search_name.ilike(search_name)).existed()

    def get_all(self):
        """
        gets all persons.

        :rtype: list[PersonEntity]
        """

        return self._get_all()

    def delete(self, id):
        """
        deletes a person with given id.

        :param int id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        for name, handler in self._handlers:
            handler.delete(id)

        store = get_current_store()
        return store.query(PersonEntity.id).filter(PersonEntity.id == id).delete()

    def get_by_name(self, first_name, last_name):
        """
        gets a person by its first and last name.

        it returns None if person does not exist.

        :param str first_name: first name.
        :param str last_name: last name

        :rtype: PersonEntity
        """

        search_name = self._get_search_name(first_name, last_name)
        store = get_current_store()
        return store.query(PersonEntity).filter(
            PersonEntity.search_name.ilike(search_name)).one_or_none()
