# -*- coding: utf-8 -*-
"""
updater handlers mixin module.
"""

import re

from pyrin.core.structs import CoreObject


class IMDBHighQualityImageFetcherMixin(CoreObject):
    """
    imdb high quality image fetcher mixin.
    """

    IMAGE_URL_REGEX = re.compile(r'(https?://([^/]+/)+[^/]+\._V1_)[^/]*(\.[^/]+)$',
                                 re.IGNORECASE)

    def get_high_quality_image_url(self, url):
        """
        gets the high quality image url from given url.

        it gets the same url if it could not extract high quality url.

        :param str url: original url.

        :rtype: str
        """

        matched = self.IMAGE_URL_REGEX.match(url)
        if matched:
            base = matched.group(1)
            extension = matched.group(3)
            return '{base}{extension}'.format(base=base, extension=extension)

        return url
