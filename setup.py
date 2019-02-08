#!/usr/bin/env python

from setuptools import setup
import os
import sys

PACKAGE_PATH = 'src'

sys.path.insert(0, PACKAGE_PATH)
import naturalsortfield

setup(
    name='django-naturalsortfield',
    url='https://github.com/emilsas/django-naturalsortfield',
    version=naturalsortfield.version_string(),
    description='Better ordering for Django CharFields.',
    long_description=open('README.txt').read(),
    
    author='Emil Santurio',
    author_email='emilsas@gmail.com',
    
    packages=['naturalsortfield'],
    package_dir={'': PACKAGE_PATH},
)
