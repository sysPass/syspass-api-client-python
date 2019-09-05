#!/bin/bash

set -e
set -x

python setup.py test

if [[ $BUILD_WHEEL == 'true' ]]; then
    cibuildwheel --output-dir dist
fi

if [[ $BUILD_SDIST == 'true' ]]; then
    python setup.py sdist
fi