# -*- coding: utf-8 -*-
"""
utils path module.
"""

import os


def get_last_directory(full_path):
    """
    gets the last directory of given path.

    :param str full_path: full path of file or directory.

    :rtype: str
    """

    if os.path.isdir(full_path):
        # this is to ensure that path ends with '/'.
        full_path = os.path.join(full_path, '')

    return os.path.basename(os.path.dirname(full_path))
