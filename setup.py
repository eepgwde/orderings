#!/usr/bin/env python
# $Id: a5f8710e0bb830ebf6d93b81030696d5e591f738 $

from setuptools import setup

setup(
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    install_requires=[
          'markdown',
          'unidecode',
          'cached-property',
    ],
    pbr=True,
)
