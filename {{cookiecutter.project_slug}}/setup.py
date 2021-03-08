#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""{{cookiecutter.project_name}}
{{cookiecutter.short_description}}
"""

import sys
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

exec(open("src/{{cookiecutter.package_name}}/_version.py").read())

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

short_description = __doc__.split("\n")

with open("README.md", "r") as handle:
    long_description = handle.read()


setup(
    name="{{ cookiecutter.package_name }}",
    version=__version__,
    short_description=short_description[1],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.url }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.__main__:main"
        ]
    },
    license="{{cookiecutter.open_source_license}}",
    setup_requires=[] + pytest_runner,
    install_requires=[
        # Basic libs
        "matplotlib>3",
        "pandas>1",
        "jupyter",
        # Extra - uncomment to use or add more
        # "scikit-learn",
        # "skimage",
        # "seaborn",
        # "pymc3"
    ],
    python_requires=">=3.6",
)
