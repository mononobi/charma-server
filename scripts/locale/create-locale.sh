#!/bin/bash

locale_name=$1

locale_name_length=${#locale_name}
if [ "$locale_name_length" = "0" ]
then
    echo "Please provide the locale name with create-locale command."
    exit 1
fi

# preventing multiple create-locale calls.
if [ -d "../../src/imovie/locale/$locale_name" ]
then
   echo "There is already a '$locale_name' locale in the application locale folder."
   echo "If you want to recreate the '$locale_name' locale, you must delete the old '$locale_name' directory first."
   exit 1
fi

pybabel init -i ../../src/imovie/locale/messages.pot -d ../../src/imovie/locale/ -l "$locale_name"
