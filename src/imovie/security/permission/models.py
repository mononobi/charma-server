# -*- coding: utf-8 -*-
"""
permission models module.
"""

from sqlalchemy import Unicode, SmallInteger, String

from pyrin.core.context import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.model.schema import CoreColumn


class PermissionBaseEntity(CoreEntity):
    """
    permission base entity class.
    """

    __tablename__ = 'permission'

    subsystem_code = CoreColumn(name='subsystem_code', type_=String(5),
                                primary_key=True, nullable=False, index=True)
    access_code = CoreColumn(name='access_code', type_=SmallInteger,
                             primary_key=True, nullable=False, index=True)
    sub_access_code = CoreColumn(name='sub_access_code', type_=SmallInteger,
                                 primary_key=True, nullable=False, index=True)

    def primary_key(self):
        """
        gets the primary key of this instance.

        :returns: tuple(str subsystem_code,
                        int access_code,
                        int sub_access_code)

        :rtype: tuple
        """

        return self.subsystem_code, self.access_code, self.sub_access_code


class PermissionEntity(PermissionBaseEntity):
    """
    permission entity class.
    """

    __table_args__ = DTO(extend_existing=True)

    description = CoreColumn(name='description', type_=Unicode(100), nullable=False)
