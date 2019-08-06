#!/usr/bin/env python3

from setuptools import setup, find_packages, Extension

import os
import io
import re

def read(*names, **kwargs):
    '''
        convenience function to extract version from __init__.py file
    '''
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    '''
        Find the version based on the string in __init__.py
    '''
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name = 'combat',
    version = find_version('combat','__init__.py'),
    packages = find_packages(),
    scripts = [
    ],
    ext_modules = [],
    cmdclass = {
    },
    package_data = {
    },
    python_requires='>=3.6',
    setup_requires = [
    ],
    include_dirs=[],
    install_requires = [		
        'patsy<=0.5.1',
        'pandas<=0.23.4'
    ],
    extras_require={
        'docs' : [
        ]
    },
    dependency_links = [
    ],
    include_package_data=True,

    author = '',
    author_email = '',
    description = 'Batch Correction using Combat Implemented in Python',
    license = "MIT License",
    url = ''
)
