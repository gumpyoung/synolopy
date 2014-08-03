#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='synolopy',
    version='0.1.0',
    description='Synology Python API',
    author='T. Havel',
    packages=find_packages(),
    requires=[
        'requests'
    ],
)