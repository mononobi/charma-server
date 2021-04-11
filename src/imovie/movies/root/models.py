# -*- coding: utf-8 -*-
"""
movies root models module.
"""

from pyrin.core.enumerations import CoreEnum
from pyrin.database.model.declarative import CoreEntity
from pyrin.database.orm.sql.schema.columns import GUIDPKColumn, SmallIntegerColumn, \
    StringColumn


class MovieRootPathBaseEntity(CoreEntity):
    """
    movie root path base entity class.
    """

    _table = 'movie_root_path'

    id = GUIDPKColumn(name='id')


class MovieRootPathEntity(MovieRootPathBaseEntity):
    """
    movie root path entity class.
    """

    _extend_existing = True

    class OSEnum(CoreEnum):
        """
        os enum.
        """

        LINUX = 0
        WINDOWS = 1
        MAC = 2
        JAVA = 3

    path = StringColumn(name='path', max_length=250, nullable=False, validated=True)
    os = SmallIntegerColumn(name='os', nullable=False, validated=True, check_in=OSEnum.values())

    _unique_on = os, path
