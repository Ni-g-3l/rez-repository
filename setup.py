from __future__ import print_function, with_statement
from setuptools import setup, find_packages


setup(
    name="rez_repository",
    version="0.1.0",
    package_dir={
        "rez_repository": "rez_repository"
    },
    packages=find_packages(where="."),
)
