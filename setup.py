#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from justwatch import __author__, __version__

with open("README.rst", "r") as fp:
    long_description = fp.read()

setup(
    name="just-watch",
    author=__author__,
    author_email="takemehighermore@gmail.com",
    description="Python utility to watch the file modification only.",
    long_description=long_description,
    version=__version__,
    license="MIT License",
    url="https://github.com/alice1017/JustWatch",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ]
)
