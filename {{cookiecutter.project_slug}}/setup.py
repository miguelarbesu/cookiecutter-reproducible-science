#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""{{cookiecutter.project_name}}
{{cookiecutter.short_description}}
"""

from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

short_description = __doc__.split("\n")

with open("README.md", "r") as handle:
    long_description = handle.read()

setup(
    name="{{ cookiecutter.module_name }}",
    version="0.1.0",
    short_description=short_description[1],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.url }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.module_name }} = {{ cookiecutter.module_name }}.__main__:main"
        ]
    },
    license="{{cookiecutter.open_source_license}}",
)
