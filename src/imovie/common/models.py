# -*- coding: utf-8 -*-
"""
common models module.
"""

from sqlalchemy import BigInteger

from pyrin.core.context import DTO
from pyrin.database.model.base import CoreEntity
from pyrin.database.model.schema import CoreColumn


class UserBaseEntity(CoreEntity):
    """
    user base entity class.
    """

    __tablename__ = 'user'

    id = CoreColumn(name='id', type_=BigInteger, autoincrement=False, primary_key=True)

    def __eq__(self, other):
        if isinstance(other, UserBaseEntity):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return '<{module}.{class_} [{pk}]>'.format(module=self.__module__,
                                                   class_=self.__class__.__name__,
                                                   pk=str(self.id))

    def __str__(self):
        return str(self.id)


class UserEntity(UserBaseEntity):
    """
    user entity class.
    """

    __table_args__ = DTO(extend_existing=True)
