# -*- coding: utf-8 -*-
"""
permission manager module.
"""

import pyrin.utils.sqlalchemy as sqlalchemy_utils

from pyrin.utils.sqlalchemy import add_like_clause, add_date_range_clause, entity_to_dict_list
from pyrin.database.services import get_current_store
from pyrin.security.permission.manager import PermissionManager as PermissionManagerBase

from imovie.security.permission.models import PermissionEntity


class PermissionManager(PermissionManagerBase):
    """
    permission manager class.
    """

    def __init__(self):
        """
        initializes an instance of PermissionManager.
        """

        PermissionManagerBase.__init__(self)

    def synchronize_all(self, **options):
        """
        synchronizes all permissions with database.
        it creates or updates the available permissions.
        """

        entities = [permission.to_entity() for permission in self.get_permissions()]
        needs_update = [entity for entity in entities if
                        self._exists(*entity.primary_key()) is True]
        needs_insert = list(set(entities).difference(set(needs_update)))

        if needs_insert:
            self._bulk_insert(needs_insert)
        if needs_update:
            self._bulk_update(needs_update)

    def _exists(self, subsystem_code, access_code, sub_access_code):
        """
        gets a value indicating that given permission exists in database.

        :rtype: bool
        """

        store = get_current_store()
        query = store.query(PermissionEntity.subsystem_code,
                            PermissionEntity.access_code,
                            PermissionEntity.sub_access_code)\
            .filter(PermissionEntity.subsystem_code == subsystem_code,
                    PermissionEntity.access_code == access_code,
                    PermissionEntity.sub_access_code == sub_access_code)
        permission_count = sqlalchemy_utils.count(query)

        return permission_count > 0

    def _make_find_clause(self, **filters):
        """
        makes the required find clauses based on
        given filters and returns the clauses list.

        :keyword str subsystem_code: subsystem code.
        :keyword int access_code: access code.
        :keyword int sub_access_code: sub access code.
        :keyword str description: description.
        :keyword datetime create_date: create date.
        :keyword datetime create_date_lower: create date lower.
        :keyword datetime create_date_upper: create date upper.

        :keyword bool consider_begin_of_day: consider begin of day for
                                             all date value lower bounds.
                                             defaults to True if not provided.

        :keyword bool consider_end_of_day: consider end of day for
                                           all date value upper bounds.
                                           defaults to True if not provided.

        :rtype: list
        """

        clauses = []

        subsystem_code = filters.get('subsystem_code', None)
        access_code = filters.get('access_code', None)
        sub_access_code = filters.get('sub_access_code', None)
        description = filters.get('description', None)
        create_date = filters.get('create_date', None)
        create_date_lower = filters.get('create_date_lower', None)
        create_date_upper = filters.get('create_date_upper', None)

        if subsystem_code is not None:
            clauses.append(PermissionEntity.subsystem_code == subsystem_code)

        if access_code is not None:
            clauses.append(PermissionEntity.access_code == access_code)

        if sub_access_code is not None:
            clauses.append(PermissionEntity.sub_access_code == sub_access_code)

        if description is not None:
            add_like_clause(clauses, PermissionEntity.description, description)

        if create_date is not None:
            add_date_range_clause(clauses, PermissionEntity.create_date,
                                  create_date, create_date)

        if create_date_lower is not None or create_date_upper is not None:
            add_date_range_clause(clauses, PermissionEntity.create_date,
                                  create_date_lower, create_date_upper, **filters)

        return clauses

    def _bulk_insert(self, entities):
        """
        bulk inserts the given permission entities.

        :param list[CorePermission] entities: permission entities to be inserted.
        """

        store = get_current_store()
        store.bulk_insert_mappings(PermissionEntity, entity_to_dict_list(entities, False))
        store.commit()

    def _bulk_update(self, entities):
        """
        bulk updates the given permission entities.

        :param list[CorePermission] entities: permission entities to be updated.
        """

        store = get_current_store()
        store.bulk_update_mappings(PermissionEntity, entity_to_dict_list(entities, False))
        store.commit()
