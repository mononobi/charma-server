# -*- coding: utf-8 -*-
"""
main entry point for imovie server.
it should be run without debug flag in production environments.
"""

from imovie import IMovieApplication

app = IMovieApplication()

# the if condition is to ensure that multiprocessing
# on windows works as expected.
if __name__ == '__main__':
    app.run(use_reloader=False)
