#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(
    name="{{ cookiecutter.module_name }}",
    version="0.1.0",
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.full_name }}{{ cookiecutter.project_slug }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.module_name }} = {{ cookiecutter.module_name }}.__main__:main"
        ]
    },
)
