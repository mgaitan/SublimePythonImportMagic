# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup

import importmagic

readme = open('README.md').read()


setup(
    # py2 + setuptools asserts isinstance(name, str) so this needs str()
    name=str('importmagic'),
    version=importmagic.__version__,
    description='Fix imports',
    long_description=readme,
    author=importmagic.__author__,
    packages=find_packages(exclude=['tests*']),
    keywords='importmagic',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
