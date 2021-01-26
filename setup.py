#!/usr/bin/env python3
from setuptools import setup
from setuptools import find_packages 

setup(
    author='Paul Bergene',
    author_email='paul@snowcrashed.net',
    url='https://snowcrashed.net',
    name='firstline',
    version='0.1',
    py_modules=['firstline'],
    packages=find_packages(),
    package_dir={'firstline'}
    install_requires=[
        'Click',
    ],
)
