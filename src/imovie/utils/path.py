# -*- coding: utf-8 -*-
"""
utils path module.
"""

from os import path


def get_file_extension(file, **options):
    """
    gets the extension of given file.

    :param str file: file path to get its extension.

    :keyword bool remove_dot: specifies that the extension must not
                              include the `.` character.
                              defaults to True if not provided.

    :rtype: str
    """

    remove_dot = options.get('remove_dot', True)
    name, extension = path.splitext(file)

    if remove_dot is not False:
        extension = extension.replace('.', '')

    return extension.lower()


def get_file_size(file, **options):
    """
    gets the file size in bytes.

    :param str file: file path to get its size.

    :rtype: int
    """

    return path.getsize(file)
