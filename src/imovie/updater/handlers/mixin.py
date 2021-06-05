# -*- coding: utf-8 -*-
"""
updater handlers mixin module.
"""

import re

import pyrin.utils.regex as regex_utils

from pyrin.core.structs import CoreObject


class ImageFetcherMixin(CoreObject):
    """
    image fetcher mixin class.
    """

    IMAGE_SIZE_PATTERN = 'UX{width}_CR0,0,{width},{height}_AL_'
    IMAGE_URL_REGEX = re.compile(r'(https?://([^/]+/)+[^/]+\._V1_)[^/]*(\.[^/]+)$',
                                 re.IGNORECASE)

    def _get_split_original_image_url(self, url):
        """
        gets the split form of original image url from given url.

        it returns two parts. first part is the url without extension
        and the second part is the extension including dot.

        it may return None for each part if it could not extract
        original url from given url.

        :param str url: image url.

        :rtype: str
        """

        if url is not None:
            matched = self.IMAGE_URL_REGEX.match(url)
            if matched:
                base = matched.group(1)
                extension = matched.group(3)
                return base, extension

        return None, None

    def get_original_image_url(self, url):
        """
        gets the original image url from given url.

        it may return None if it could not extract original url.

        :param str url: image url.

        :rtype: str
        """

        base, extension = self._get_split_original_image_url(url)
        if base is not None and extension is not None:
            return '{base}{extension}'.format(base=base, extension=extension)

        return None

    def get_resized_image_url(self, url, width, height):
        """
        gets the resized image from given url.

        :param str url: image url.
        :param int width: width of requested image.
        :param int height: height of requested image.

        :rtype: str
        """

        resized_url = None
        base, extension = self._get_split_original_image_url(url)
        if base is not None and extension is not None:
            size = self.IMAGE_SIZE_PATTERN.format(width=width, height=height)
            resized_url = '{base}{size}{extension}'.format(base=base, size=size,
                                                           extension=extension)

        return resized_url


class ImageSetFetcherMixin(CoreObject):
    """
    image set fetcher mixin class.
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
