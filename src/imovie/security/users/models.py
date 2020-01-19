# -*- coding: utf-8 -*-
"""
common models module.
"""

from sqlalchemy import Unicode, TIMESTAMP, CheckConstraint, SmallInteger

import pyrin.globalization.datetime.services as datetime_services

from pyrin.core.context import DTO
from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.base import CoreEntity
from pyrin.database.model.schema import CoreColumn
from pyrin.database.orm.types.custom import GUID


class UserBaseEntity(CoreEntity):
    """
    user base entity class.
    """

    __tablename__ = 'user'

    id = CoreColumn(name='id', type_=GUID, primary_key=True, nullable=False, index=True)

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

    class StatusEnum(CoreEnum):
        """
        status enum.
        """

        NOT_APPROVED = 0
        APPROVED = 1
        SUSPENDED = 2
        DELETED = 3

    user_name = CoreColumn(name='user_name', type_=Unicode(50), nullable=False, unique=True)
    password_hash = CoreColumn(name='password_hash', type_=Unicode(250),
                               nullable=False, exposed=False)
    first_name = CoreColumn(name='first_name', type_=Unicode(50), nullable=False)
    last_name = CoreColumn(name='last_name', type_=Unicode(50), nullable=False)
    email = CoreColumn(name='email', type_=Unicode(100), nullable=False, unique=True)
    create_date = CoreColumn(name='create_date', type_=TIMESTAMP(timezone=True),
                             nullable=False, default=datetime_services.now)
    status = CoreColumn(CheckConstraint('status in {values}'.
                                        format(values=tuple(StatusEnum.values()))),
                        name='status', type_=SmallInteger,
                        nullable=False, default=StatusEnum.NOT_APPROVED)
    last_login_date = CoreColumn(name='last_login_date', type_=TIMESTAMP(timezone=True))
    wrong_password_count = CoreColumn(name='wrong_password_count', type_=SmallInteger,
                                      nullable=False, default=0)
