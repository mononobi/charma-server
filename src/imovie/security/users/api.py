# -*- coding: utf-8 -*-
"""
users api module.
"""

from pyrin.api.router.decorators import api

from imovie.security.users.permissions import DELETE_USER_LIST_PERMISSION


@api('/users/test', permissions=[DELETE_USER_LIST_PERMISSION], login_required=False)
def test(**options):
    pass
