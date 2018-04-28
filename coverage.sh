#!/bin/sh

coverage run --branch --source bootini_star -m unittest
coverage html -d tmp/coverage
