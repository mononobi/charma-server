# -*- coding: utf-8 -*-
"""
updater handlers storyline module.
"""

from imovie.updater.decorators import updater
from imovie.updater.handlers.base import UpdaterBase


@updater()
class IMDBStoryLineUpdater(UpdaterBase):
    """
    imdb storyline updater class.
    """

    _name = 'imdb_storyline'
    _category = 'storyline'

    def _fetch(self, url, content, **options):
        """
        fetches data from given url.

        :param str url: url to fetch info from it.
        :param bs4.BeautifulSoup content: the html content of input url.

        :returns: imdb storyline.
        """

        storyline = None
        storyline_section = content.find('div', class_='article', id='titleStoryLine')
        if storyline_section is not None:
            storyline_container = storyline_section.find('div', class_='inline canwrap')
            if storyline_container is not None:
                storyline_tag = storyline_container.find('span')
                if storyline_tag is not None:
                    storyline = storyline_tag.get_text(strip=True)

        return storyline
