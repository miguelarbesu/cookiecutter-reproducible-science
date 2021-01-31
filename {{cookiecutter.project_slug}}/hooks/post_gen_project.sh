#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Spin a virtual env
# TODO
# Install dev dependencies
pip install -r devtools/requirements-dev.txt
# Configure pre-commit
pre-commit install -c devtools/pre-commit-config.yaml
# Start git
git init
git add .
git commit -m "Initial commit"
