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


def get_last_directory(full_path):
    """
    gets the last directory of given path.

    :param str full_path: full path of file or directory.

    :rtype: str
    """

    if path.isdir(full_path):
        # this is to ensure that path ends with '/'.
        full_path = path.join(full_path, '')

    return path.basename(path.dirname(full_path))
