#!/bin/bash

# preventing multiple init-catalog calls.
if [ -d "../../src/imovie/locale" ]
then
   echo "There is already a locale directory in the application folder."
   echo "If you want to init-catalog again, you must delete the old locale directory first."
   exit 1
fi

mkdir ../../src/imovie/locale
pybabel extract -o ../../src/imovie/locale/messages.pot ../../src/imovie/ ../../src/pyrin/
