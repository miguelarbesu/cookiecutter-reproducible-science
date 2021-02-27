#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# Spin a virtual env
# TODO
# Install dev dependencies
pip install -r devtools/requirements-dev.txt
# Start git
git init
git branch -m main
# Start versioneer
versioneer install
# Build documentation
mkdocs build
# Do initial commit
git add .
git commit -m "Initial commit"
git tag -a {{cookiecutter.version}} -m "First version"
# Configure pre-commit
pre-commit install
pre-commit autoupdate
printf "Please do\pre-commit run --all-files\to format all before the next commit."