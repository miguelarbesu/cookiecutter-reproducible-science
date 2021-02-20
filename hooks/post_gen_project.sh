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
git tag -a v{cookiecutter.version} -m "First version"
# Configure pre-commit
pre-commit install
pre-commit autoupdate
