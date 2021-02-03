#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Spin a virtual env
# TODO
# Install dev dependencies
pip install -r devtools/requirements-dev.txt
# Start git
git init
git branch -m main
git add .
git commit -m "Initial commit"
# Configure pre-commit
pre-commit install -c devtools/pre-commit-config.yaml