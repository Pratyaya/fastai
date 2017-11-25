
# coding: utf-8

"""
Setup script for installing fastai
"""

##########################################################################
## Imports
##########################################################################

from distutils.core import setup


##########################################################################
## Setup
##########################################################################

setup(
    name = "fastai",

    packages = ['fastai'], # this must be the same as the name above

    version = 0.47 ,

    description = "The fast.ai deep learning library, lessons, and tutorials",
    
    author = "Jeremy Howard, Rachel Thomas, Yannet Interian and many others",
    
    author_email = "j@fast.ai",
    
    url = "https://github.com/groverpr/fastai",
    
    download_url =  'https://github.com/groverpr/fastai/archive/0.47.tar.gz',

    install_requires = 
     ['scipy',
    'numpy',
    'pillow',
    'jpeg',
    'spacy',
    'zlib',
    'freetype',
    'libtiff',
    'bleach',
    'certifi',
    'cffi',
    'cycler',
    'decorator',
    'entrypoints',
    'expat',
    'fontconfig',
    'glib',
    'html5lib',
    'icu',
    'ipykernel',
    'ipython',
    'ipython_genutils',
    'ipywidgets',
    'jbig',
    'jedi',
    'jinja2',
    'jsonschema',
    'jupyter',
    'jupyter_client',
    'jupyter_console',
    'jupyter_core',
    'libffi',
    'libgcc',
    'libgfortran',
    'libiconv',
    'libpng',
    'libsodium',
    'libxml2',
    'markupsafe',
    'matplotlib',
    'mistune',
    'mkl',
    'nbconvert',
    'nbformat',
    'notebook',
    'numpy',
    'olefile',
    'openssl',
    'pandas',
    'pandocfilters',
    'path.py',
    'patsy',
    'pcre',
    'pexpect',
    'pickleshare',
    'pillow',
    'pip',
    'prompt_toolkit',
    'ptyprocess',
    'pycparser',
    'pygments',
    'pyparsing',
    'pyqt',
    'python-dateutil',
    'pytz',
    'pyzmq',
    'qt',
    'qtconsole',
    'readline',
    'scipy',
    'seaborn',
    'setuptools',
    'simplegeneric',
    'sip',
    'six',
    'sqlite',
    'statsmodels',
    'terminado',
    'testpath',
    'tk',
    'tornado',
    'tqdm',
    'traitlets',
    'wcwidth',
    'wheel',
    'widgetsnbextension',
    'xz',
    'zeromq',
    'pytorch>=0.2.0',
    'torchvision>=0.1.9',
    'bcolz',
    'prompt_toolkit',
    'opencv-python',
    'isoweek',
    'pandas_summary',
    'torchtext',
    'graphviz',
    'sklearn_pandas',
    'feather-format',
    'jupyter_contrib_nbextensions',
    'plotnine',
    'docrepr',
    'awscli',
    'kaggle-cli',
    'ipywidgets',
    'jupyter_contrib_nbextensions'],

    keywords = ['deeplearning', 'pytorch', 'machinelearning'],

    classifiers = ['Development Status :: 3 - Alpha',
                      'Programming Language :: Python',
                    'Programming Language :: Python :: 3.6',]
)
