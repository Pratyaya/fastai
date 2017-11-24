
# coding: utf-8

"""
Setup script for installing fastai
"""

##########################################################################
## Imports
##########################################################################

import os
import re
import codecs

from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################

## Basic information
NAME         = "fastai"
DESCRIPTION  = "The fast.ai deep learning library, lessons, and tutorials"
AUTHOR       = "Jeremy Howard, Rachel Thomas, Yannet Interian and many others"
EMAIL        = "j@fast.ai"
URL   = "https://github.com/fastai/fastai.git"
#download_url = 'https://github.com/groverpr/fastai/archive/0.45.tar.gz'
PACKAGE      = "fastai"
REPOSITORY   = "https://github.com/groverpr/fastai"
VERSION   = 0.45

## Define the keywords
KEYWORDS     = (
    'deeplearning', 'machinelearning', 'pytorch'
)

## Define the classifiers
CLASSIFIERS = ['Development Status :: 3 - Alpha'
			]

## Important Paths
PROJECT      = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"

## Directories to ignore in find_packages
EXCLUDES     = (
    "tests", "bin", "docs", "fixtures", "register", "notebooks",
)

##########################################################################
## Helper Function
##########################################################################

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()

def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line

##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": VERSION ,
    "description": DESCRIPTION,
    "author": AUTHOR,
    "author_email": EMAIL,
    "url": REPOSITORY,
    "download_url": "{}/tarball/v{}".format(REPOSITORY, VERSION),
    "install_requires": list(get_requires()),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)

