#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Spin a virtual env
# TODO
# Install dev dependencies
pip install -r devtools/requirements-dev.txt
# Configure pre-commit
pre-commit install
pre-commit autoupdate
# Start versioneer
versioneer install
# Format new versioneer files
pre-commit run --all-files
# Build documentation
mkdocs build
# Start git
git init
git branch -m main
git add .
git commit -m "Initial commit"
git tag -a {{cookiecutter.version}} -m "First version"