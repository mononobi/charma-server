# -*- coding: utf-8 -*-
"""
start module.
"""

from imovie import IMovieApplication


app = IMovieApplication()


if __name__ == '__main__':
    app.run(use_reloader=False, threaded=True)
