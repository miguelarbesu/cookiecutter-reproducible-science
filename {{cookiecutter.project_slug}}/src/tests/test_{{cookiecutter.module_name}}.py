"""
Unit and regression test for the {{cookiecutter.package_name}} package.
"""

# Import package, test suite, and other packages as needed
import {{cookiecutter.package_name}}
import pytest
import sys


def test_{{cookiecutter.package_name}}_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "{{cookiecutter.package_name}}" in sys.modules