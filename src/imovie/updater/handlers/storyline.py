# -*- coding: utf-8 -*-
"""
updater handlers storyline module.
"""

from imovie.updater.decorators import updater
from imovie.updater.enumerations import UpdaterCategoryEnum
from imovie.updater.handlers.base import UpdaterBase


@updater()
class StoryLineUpdater(UpdaterBase):
    """
    storyline updater class.
    """

    _category = UpdaterCategoryEnum.STORYLINE

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

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
