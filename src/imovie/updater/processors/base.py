# -*- coding: utf-8 -*-
"""
updater processors base module.
"""

from imovie.updater.interface import AbstractProcessor


class ProcessorBase(AbstractProcessor):
    """
    processor base class.
    """

    # the category of this processor.
    # it is actually the relevant entity's column name.
    _category = None

    @property
    def name(self):
        """
        gets the name of this processor.

        :rtype: str
        """

        return self.get_name()

    @property
    def category(self):
        """
        gets the category of this processor.

        :rtype: str
        """

        return self._category
