# -*- coding: utf-8 -*-
"""
updater handlers mixin module.
"""

import re

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

        it may return None if it could not extract original url.

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
