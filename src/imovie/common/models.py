# -*- coding: utf-8 -*-
"""
common models module.
"""

from sqlalchemy import Column, BigInteger

from pyrin.core.context import DTO
from pyrin.database.model.base import CoreEntity


class UserBaseEntity(CoreEntity):
    """
    user base entity class.
    """

    __tablename__ = 'users'
    __primary_key_sequence__ = 'users_id_seq'

    id = Column(name='id', type_=BigInteger, autoincrement=False, primary_key=True)


class UserEntity(UserBaseEntity):
    """
    user entity class.
    """

    __table_args__ = DTO(extend_existing=True)
