# -*- coding: utf-8 -*-
"""
actors models module.
"""

from sqlalchemy import Unicode, Integer, ForeignKey, CheckConstraint

from pyrin.database.model.base import CoreEntity
from pyrin.database.orm.sql.schema.base import CoreColumn
