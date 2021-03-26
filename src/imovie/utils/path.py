# -*- coding: utf-8 -*-
"""
utils path module.
"""

import os


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
    name, extension = os.path.splitext(file)

    if remove_dot is not False:
        extension = extension.replace('.', '')

    return extension.lower()


def get_file_size(file, **options):
    """
    gets the file size in bytes.

    :param str file: file path to get its size.

    :rtype: int
    """

    return os.path.getsize(file)


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


def get_files(directory, *extensions):
    """
    gets a list of all files in given directory.

    it could filter files with given extensions if provided.

    :param str directory: full path of directory.
    :param str extensions: extension of files to be listed.
                           if not provided, all files will be listed.

    :rtype: list[str]
    """

    extensions = tuple(item.lower() for item in extensions)
    files = []
    for root, directories, file_names in os.walk(directory):
        for item in file_names:
            extension = get_file_extension(item)
            if len(extensions) > 0 and extension not in extensions:
                continue
            full_path = os.path.join(root, item)
            files.append(full_path)
        break

    return files


def get_directories(root):
    """
    gets a list of all directories in given root directory.

    :param str root: root path.

    :rtype: list[str]
    """

    folders = []
    for root, directories, file_names in os.walk(root):
        for item in directories:
            full_path = os.path.join(root, item)
            folders.append(full_path)
        break

    return folders
