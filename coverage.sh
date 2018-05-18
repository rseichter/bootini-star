#!/bin/sh

function _coverage {
    APP_SETTINGS=bootini_star.config.Testing ONLINE_TESTS=1 LOG_LEVEL=fatal venv/bin/coverage $*
}

_coverage run --branch --source bootini_star -m unittest
_coverage html -d tmp/coverage
