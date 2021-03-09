# -*- coding: utf-8 -*-
"""
movies related actors models module.
"""

from sqlalchemy import Unicode, Integer

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, GUIDPKColumn, \
    SequencePKColumn, FKColumn, IntegerColumn, SmallIntegerColumn, DateColumn, \
    TimeStampColumn, DateTimeColumn, BooleanColumn, HiddenColumn, StringColumn, \
    TextColumn, BigIntegerColumn
