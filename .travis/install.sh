#!/bin/bash

set -e
set -x

if [[ $BUILD_WHEEL == 'true' ]]; then
    pip install wheel cibuildwheel==0.9.4
fi