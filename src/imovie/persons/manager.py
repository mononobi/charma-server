# -*- coding: utf-8 -*-
"""
persons manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.utils.misc as misc_utils

from pyrin.core.globals import _
from pyrin.core.structs import Manager, Context
from pyrin.database.services import get_current_store

from imovie.persons import PersonsPackage
from imovie.persons.handler import AbstractPersonHandler
from imovie.persons.models import PersonEntity
from imovie.persons.queries import PersonsQueries
from imovie.persons.exceptions import PersonDoesNotExistError, InvalidPersonHandlerTypeError, \
    PersonHandlerNameRequiredError, DuplicatedPersonHandlerError, PersonHandlerNotExistedError


class PersonsManager(Manager, PersonsQueries):
    """
    persons manager class.
    """

    package_class = PersonsPackage

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
            raise PersonHandlerNotExistedError('Person type [{name}] does not exist.'
                                               .format(name=name))

        return self._handlers.get(name)

    def _get(self, id):
        """
        gets person with given id.

        it returns None if person does not exist.

        :param uuid.UUID id: person id.

        :rtype: PersonEntity
        """

        store = get_current_store()
        return store.query(PersonEntity).get(id)

    def _prepare_handlers(self, options):
        """
        prepares person handlers to be usable as a list, if it is present in given inputs.

        inputs will be modified in-place.

        :keyword str | list[str] type: person type to be used.
                                       defaults to None if not provided.
        """

        handler = options.get('type')
        if handler is not None and not isinstance(handler, list):
            result = misc_utils.make_iterable(handler, list)
            options.update(type=result)

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
            raise PersonHandlerNameRequiredError('Person handler name for '
                                                 '[{instance}] must be provided.'
                                                 .format(instance=instance))

        if instance.name is self._handlers:
            raise DuplicatedPersonHandlerError('There is another registered person handler '
                                               'with name [{name}], so new handler '
                                               '[{instance}] could not be registered.'
                                               .format(name=instance.name, instance=instance))

        self._handlers[instance.name] = instance

    def get(self, id):
        """
        gets person with given id.

        it raises an error if person does not exist.

        :param uuid.UUID id: person id.

        :raises PersonDoesNotExistError: person does not exist error.

        :rtype: PersonEntity
        """

        entity = self._get(id)
        if entity is None:
            raise PersonDoesNotExistError(_('Person with id [{id}] does not exist.')
                                          .format(id=id))
        return entity

    def create(self, fullname, **options):
        """
        creates a new person.

        :param str fullname: fullname.

        :keyword str imdb_page: imdb page link.
        :keyword str photo_name: photo file name.

        :keyword str | list[str] type: person type to be used.
                                       defaults to None if not provided.

        :raises ValidationError: validation error.

        :returns: created person id.
        :rtype: uuid.UUID
        """

        options.update(fullname=fullname)
        self._prepare_handlers(options)
        validator_services.validate_dict(PersonEntity, options)
        entity = PersonEntity(**options)
        entity.search_name = self._get_search_name(fullname)
        entity.identifier = self._get_identifier(options.get('imdb_page')) or None
        entity.save()

        handlers = options.get('type')
        if handlers is not None:
            for name in handlers:
                handler = self._get_handler(name)
                handler.create(entity.id, **options)

        return entity.id

    def update(self, id, **options):
        """
        updates a person with given id.

        :param uuid.UUID id: person id.

        :keyword str fullname: fullname.
        :keyword str imdb_page: imdb page link.
        :keyword str photo_name: photo file name.

        :keyword str | list[str] type: person type to be used.
                                       defaults to None if not provided.

        :raises ValidationError: validation error.
        :raises PersonDoesNotExistError: person does not exist error.
        """

        self._prepare_handlers(options)
        validator_services.validate_dict(PersonEntity, options, for_update=True)
        entity = self.get(id)
        entity.update(**options)
        entity.search_name = self._get_search_name(entity.fullname)
        entity.identifier = self._get_identifier(entity.imdb_page) or None

        handlers = options.get('type')
        if handlers is not None:
            for name in handlers:
                handler = self._get_handler(name)
                handler.update(entity.id, **options)

    def delete(self, id):
        """
        deletes a person with given id.

        :param uuid.UUID id: person id.

        :returns: count of deleted items.
        :rtype: int
        """

        for name, handler in self._handlers.items():
            handler.delete(id)

        store = get_current_store()
        return store.query(PersonEntity.id).filter(PersonEntity.id == id).delete()
