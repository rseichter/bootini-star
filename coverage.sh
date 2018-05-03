#!/bin/sh

COV='venv/bin/coverage'

$COV run --branch --source bootini_star -m unittest
$COV html -d tmp/coverage
