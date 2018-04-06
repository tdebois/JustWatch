#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from justwatch import __author__, __version__

setup(
    name="JustWatch",
    author=__author__,
    description="Just watch the file modification",
    version=__version__,
    license="MIT License",
    packages=find_packages(),
    # install_requires=[""],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ]
)
