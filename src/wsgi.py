# -*- coding: utf-8 -*-
"""
main entry point for wsgi web-server.
"""

from start import app

# the if condition is to ensure that multiprocessing
# on windows works as expected.
if __name__ == '__main__':
    app.run(use_reloader=False)
