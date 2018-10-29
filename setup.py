# -*- coding: utf-8 -*-
u"""
setup script
"""

from __future__ import unicode_literals
from __future__ import print_function


# Copyright©2017 fininfotech co, ltd., All rights reserved.
# 版权©2017 上海玢殷信息技术有限公司, 保留所有权利。

import os
import io
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()


setup(
    name='click_patch',
    version='0.0.1',
    description='',
    long_description=README,
    entry_points={
        'console_scripts': ['click_patch_cmd=click_patch.script:run'],
    },
    keywords='',
    author='',
    author_email='',
    url='www.fininfotech.com',
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    platforms=["any"],
    test_suite='tests',
    install_requires=[
    ],
    extras_require={
    }
)
