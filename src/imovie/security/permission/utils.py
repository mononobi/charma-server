# -*- coding: utf-8 -*-
"""
permission utils module.
"""

from pyrin.core.context import DTO


def get_permission_id(subsystem_code, access_code, sub_access_code):
    """
    gets the permission id using given inputs.

    :param str subsystem_code: subsystem code.
    :param int access_code: access code.
    :param int sub_access_code: sub access code.

    :returns: dict(str subsystem_code,
                   int access_code,
                   int sub_access_code)

    :rtype: dict
    """

    return DTO(subsystem_code=subsystem_code,
               access_code=access_code,
               sub_access_code=sub_access_code)


def get_permission_info(subsystem_code, access_code, sub_access_code, description):
    """
    gets the permission info using given inputs.

    :param str subsystem_code: subsystem code.
    :param int access_code: access code.
    :param int sub_access_code: sub access code.
    :param str description: description.

    :returns: dict(str subsystem_code,
                   int access_code,
                   int sub_access_code,
                   str description)

    :rtype: dict
    """

    permission_info = get_permission_id(subsystem_code, access_code, sub_access_code)
    permission_info.update(description=description)

    return permission_info


def get_permission_id_string(subsystem_code, access_code, sub_access_code):
    """
    gets the permission id string using given inputs.

    :param str subsystem_code: subsystem code.
    :param int access_code: access code.
    :param int sub_access_code: sub access code.

    :rtype: str
    """

    permission_id = get_permission_id(subsystem_code, access_code, sub_access_code)
    return '{subsystem_code}-{access_code}-{sub_access_code}'.format(**permission_id)


def get_permission_info_string(subsystem_code, access_code, sub_access_code, description):
    """
    gets the permission info string using given inputs.

    :param str subsystem_code: subsystem code.
    :param int access_code: access code.
    :param int sub_access_code: sub access code.
    :param str description: description.

    :rtype: str
    """

    permission_info = get_permission_info(subsystem_code, access_code,
                                          sub_access_code, description)

    return '{subsystem_code}-{access_code}-{sub_access_code}: ' \
           '{description}'.format(**permission_info)
