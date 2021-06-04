# -*- coding: utf-8 -*-
"""
updater handlers mixin module.
"""

import re

import pyrin.utils.regex as regex_utils

from pyrin.core.structs import CoreObject


class HighQualityImageFetcherMixin(CoreObject):
    """
    high quality image fetcher mixin.
    """

    IMAGE_URL_REGEX = re.compile(r'(https?://([^/]+/)+[^/]+\._V1_)[^/]*(\.[^/]+)$',
                                 re.IGNORECASE)

    def get_high_quality_image_url(self, url):
        """
        gets the high quality image url from given url.

        it may return None if it could not extract high quality url.

        :param str url: original url.

        :rtype: str
        """

        if url is not None:
            matched = self.IMAGE_URL_REGEX.match(url)
            if matched:
                base = matched.group(1)
                extension = matched.group(3)
                return '{base}{extension}'.format(base=base, extension=extension)

        return None


class ImageSetFetcherMixin(CoreObject):
    """
    image set fetcher mixin.
    """

    IMAGE_SET_URL_REGEX = re.compile(r'https?://[^ ]+[.][a-z]{3}', re.IGNORECASE)

    def get_highest_quality_image_url(self, image_set):
        """
        gets the highest quality image url from given image set.

        it may return None if it could not extract any urls.

        :param str image_set: image urls set.

        :rtype: str
        """

        if image_set is not None:
            matches = regex_utils.matches(self.IMAGE_SET_URL_REGEX, image_set)
            if len(matches) > 0:
                return matches[-1]

        return None


class MetadataContainerMixin(CoreObject):
    """
    metadata Container Mixin.
    """

    META_DATA_CONTAINER_REGEX = re.compile(r'^TitleBlock__TitleMetaDataContainer.*',
                                           re.IGNORECASE)
