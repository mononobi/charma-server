# -*- coding: utf-8 -*-
"""
security context module.
"""

from pyrin.core.context import DTO


class UserIdentity(DTO):
    """
    user identity class.
    this class provides a simple object to hold user identity.
    """

    def __init__(self, user_id, shop_id):
        """
        initializes an instance of UserIdentity.

        :param int user_id: user id.
        :param int shop_id: shop id.
        """

        super(UserIdentity, self).__init__()

        self.user_id = user_id
        self.shop_id = shop_id

    def __str__(self):
        return '{shop_id}-{user_id}'.format(shop_id=self.shop_id,
                                            user_id=self.user_id)
