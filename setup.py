#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def requirements(filename):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), filename))) as f:
        return f.readlines()

setup(
    name='lomakekala',
    version='0.0.0',
    description='Generic Form Generator',
    author='Santtu Pajukanta',
    author_email='santtu@pajukanta.fi',
    url='https://github.com/japsu/lomakekala',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements('requirements.txt')
)
