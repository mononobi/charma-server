# -*- coding: utf-8 -*-
"""
users permissions module.
"""

from pyrin.core.globals import _

from imovie.security.permission.base import CorePermission

GET_USER_LIST_PERMISSION = CorePermission('U', 1, 1, 'Get user list')
ADD_USER_LIST_PERMISSION = CorePermission('U', 1, 2, 'Add user list')
DELETE_USER_LIST_PERMISSION = CorePermission('U', 1, 3, 'Delete user list', _('Delete user list'))
# DUP_DELETE_USER_LIST_PERMISSION = CorePermission('U', 1, 3, 'Delete user list')
