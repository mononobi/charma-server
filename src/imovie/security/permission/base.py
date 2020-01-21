# -*- coding: utf-8 -*-
"""
permission base module.
"""

from pyrin.security.permission.base import PermissionBase

from imovie.security.permission.models import PermissionEntity
from imovie.security.permission.exceptions import PermissionDescriptionNotProvidedError, \
    PermissionSubAccessCodeNotProvidedError, PermissionAccessCodeNotProvidedError, \
    PermissionSubsystemCodeNotProvidedError, PermissionSubsystemCodeLengthError, \
    InvalidPermissionAccessCodeError, InvalidPermissionSubAccessCodeError, \
    PermissionDescriptionLengthError, PermissionLocalizedDescriptionLengthError
from imovie.security.permission.utils import get_permission_info_string, get_permission_id, \
    get_permission_id_string


class CorePermission(PermissionBase):
    """
    core permission class.
    all application permissions must be an instance of this class.
    """

    def __init__(self, subsystem_code, access_code, sub_access_code,
                 description, localized_description=None, **options):
        """
        initializes an instance of CorePermission.

        :param str subsystem_code: subsystem code.
        :param int access_code: access code.
        :param int sub_access_code: sub access code.
        :param str description: description.
        :param str localized_description: localized description.
                                          if not provided, defaults to
                                          description value.
        """

        if localized_description in (None, '') or localized_description.isspace():
            localized_description = description

        self.subsystem_code = subsystem_code
        self.access_code = access_code
        self.sub_access_code = sub_access_code
        self.description = description
        self.localized_description = localized_description
        self._validate()

        PermissionBase.__init__(self, **options)

    def __hash__(self):
        """
        gets the correct hash of current permission.

        :rtype: int
        """

        return hash(self.get_id())

    def __eq__(self, other):
        """
        gets the correct comparison between current and other permission for equality.

        :param PermissionBase other: other permission instance to be
                                     compared to the current one.

        :rtype: bool
        """

        if not isinstance(other, CorePermission):
            return False

        return self.get_id() == other.get_id()

    def __ne__(self, other):
        """
        gets the correct comparison between current and other permission for not equality.

        :param PermissionBase other: other permission instance to be
                                     compared to the current one.

        :rtype: bool
        """

        return not self == other

    def __str__(self):
        """
        gets the correct string representation of current permission.

        :rtype: str
        """

        return get_permission_info_string(self.subsystem_code, self.access_code,
                                          self.sub_access_code, self.localized_description)

    def __repr__(self):
        """
        gets the correct string representation of current permission.

        :rtype: str
        """

        return get_permission_id_string(self.subsystem_code,
                                        self.access_code, self.sub_access_code)

    def _validate(self):
        """
        validates permission attributes.

        :raises PermissionSubsystemCodeNotProvidedError: permission subsystem code
                                                         not provided error.

        :raises PermissionSubsystemCodeLengthError: permission subsystem
                                                    code length error.

        :raises PermissionAccessCodeNotProvidedError: permission access code
                                                      not provided error.

        :raises InvalidPermissionAccessCodeError: invalid permission
                                                  access code error.

        :raises PermissionSubAccessCodeNotProvidedError: permission sub access code
                                                         not provided error.

        :raises InvalidPermissionSubAccessCodeError: invalid permission sub
                                                     access code error.

        :raises PermissionDescriptionNotProvidedError: permission description
                                                       not provided error.

        :raises PermissionDescriptionLengthError: permission description
                                                  length error.

        :raises PermissionLocalizedDescriptionLengthError: permission localized
                                                           description length error.
        """

        if self.subsystem_code in (None, '') or self.subsystem_code.isspace():
            raise PermissionSubsystemCodeNotProvidedError('Permission subsystem '
                                                          'code must be provided.')

        if len(self.subsystem_code) <= 0 or len(self.subsystem_code) > 5:
            raise PermissionSubsystemCodeLengthError('Permission subsystem code '
                                                     'has an invalid length.')

        if self.access_code is None:
            raise PermissionAccessCodeNotProvidedError('Permission access code '
                                                       'must be provided.')

        if self.access_code < 1:
            raise InvalidPermissionAccessCodeError('Permission access code [{code}] is '
                                                   'invalid.'.format(code=self.access_code))

        if self.sub_access_code is None:
            raise PermissionSubAccessCodeNotProvidedError('Permission sub access '
                                                          'code must be provided.')

        if self.sub_access_code < 1:
            raise InvalidPermissionSubAccessCodeError('Permission sub access '
                                                      'code [{code}] is invalid.'
                                                      .format(code=self.sub_access_code))

        if self.description in (None, '') or self.description.isspace():
            raise PermissionDescriptionNotProvidedError('Permission description '
                                                        'must be provided.')

        if len(self.description) > 100:
            raise PermissionDescriptionLengthError('Permission description '
                                                   'has an invalid length.')

        if self.localized_description not in (None, '') or \
                not self.localized_description.isspace():
            if len(self.localized_description) > 150:
                raise PermissionLocalizedDescriptionLengthError('Permission localized '
                                                                'description has an '
                                                                'invalid length.')

    def get_id(self):
        """
        gets permission id.
        note that this object must be fully unique for each different permission.
        it is an immutable type to be usable as dict key.

        :rtype: dict
        """

        return get_permission_id(self.subsystem_code, self.access_code, self.sub_access_code)

    def to_entity(self):
        """
        gets the equivalent entity of current permission.

        :rtype: PermissionEntity
        """

        entity = PermissionEntity()
        entity.subsystem_code = self.subsystem_code
        entity.access_code = self.access_code
        entity.sub_access_code = self.sub_access_code
        entity.description = self.description

        return entity
