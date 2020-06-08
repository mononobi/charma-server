# -*- coding: utf-8 -*-
"""
start module.
"""

from imovie import IMovieApplication


app = IMovieApplication()

# the if condition is to ensure that multiprocessing
# on windows works as expected.
if __name__ == '__main__':
    app.run(use_reloader=False)
