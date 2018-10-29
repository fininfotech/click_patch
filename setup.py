# -*- coding: utf-8 -*-
u""" setup script
"""

import os
import io
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.md'), encoding="utf8").read()

setup(
    name='click_patch',
    version='0.0.1',
    description='',
    long_description=README,
    keywords='',
    author='',
    author_email='',
    url='www.fininfotech.com',
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    platforms=["any"],
    test_suite='tests',
    install_requires=[
        'click',
    ],
    extras_require={
    }
)
