#!/bin/bash

pybabel extract -o ../../src/imovie/locale/messages.pot ../../src/imovie/ ../../src/pyrin/
pybabel update -i ../../src/imovie/locale/messages.pot -d ../../src/imovie/locale/
pybabel compile -d ../../src/imovie/locale/
