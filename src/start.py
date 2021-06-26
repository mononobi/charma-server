# -*- coding: utf-8 -*-
"""
start module.
"""

from charma import CharmaApplication


app = CharmaApplication()


if __name__ == '__main__':
    app.run(use_reloader=False, threaded=True)
