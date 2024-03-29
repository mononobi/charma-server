# -*- coding: utf-8 -*-
"""
updater handlers storyline module.
"""

from charma.updater.decorators import updater
from charma.updater.enumerations import UpdaterCategoryEnum
from charma.updater.handlers.base import UpdaterBase


class StoryLineUpdaterBase(UpdaterBase):
    """
    storyline updater base class.
    """

    _category = UpdaterCategoryEnum.STORYLINE


@updater()
class StoryLineUpdater(StoryLineUpdaterBase):
    """
    storyline updater class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb storyline.
        :rtype: str
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


@updater()
class StoryLineUpdaterV2(StoryLineUpdaterBase):
    """
    storyline updater v2 class.
    """

    def _fetch(self, content, **options):
        """
        fetches data from given content.

        :param bs4.BeautifulSoup content: the html content of imdb page.

        :keyword bs4.BeautifulSoup credits: the html content of credits page.
                                            this is only needed by person updaters.

        :returns: imdb storyline.
        :rtype: str
        """

        storyline = None
        storyline_section = content.find('div', {'data-testid': 'storyline-plot-summary'})
        if storyline_section is not None:
            storyline_container = storyline_section.find('div', class_=False)
            if storyline_container is not None:
                result = self._get_text(storyline_container)
                if result is not None:
                    storyline = result

        return storyline
