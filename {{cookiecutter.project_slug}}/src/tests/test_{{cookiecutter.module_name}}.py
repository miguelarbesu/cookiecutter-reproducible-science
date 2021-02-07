"""
Unit and regression test for the {{cookiecutter.package_name}} package.
"""

import sys

# Import package, test suite, and other packages as needed
import {{cookiecutter.package_name}}
import pytest


def test_{{cookiecutter.package_name}}_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "{{cookiecutter.package_name}}" in sys.modules
