#!/usr/bin/env python3
from setuptools import setup
from setuptools import find_packages 

setup(
    author='Paul Bergene',
    author_email='paul@snowcrashed.net',
    url='https://snowcrashed.net',
    name='firstline',
    version='0.2',
    py_modules=['firstline'],
    packages=find_packages(),

    extras_require={
        'dev': [
            'pdoc3',
            'sphinx',
            'pylint'
         ]
    },

    install_requires=[
        'Click',
    ],

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Natural Language :: English'
    ]
)
