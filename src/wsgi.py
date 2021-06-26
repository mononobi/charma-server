# -*- coding: utf-8 -*-
"""
wsgi module.
"""

from charma import CharmaApplication


app = CharmaApplication()


if __name__ == '__main__':
    app.run()
