# -*- coding: utf-8 -*-
"""
wsgi module.
"""

from imovie import IMovieApplication


app = IMovieApplication()


if __name__ == '__main__':
    app.run()
