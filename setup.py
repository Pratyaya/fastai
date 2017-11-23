
# coding: utf-8

from distutils.core import setup
setup(
  name = 'fastai',
  packages = ['fastai'], # this must be the same as the name above
  version = '0.1',
  author = 'Jeremy Howard',
  author_email = 'j@fast.ai',
  description = 'The fast.ai deep learning library, lessons, and tutorials',
  url = 'https://github.com/fastai/fastai.git', # use the URL to the github repo
  download_url = 'https://github.com/groverpr/fastai/archive/0.1.tar.gz', 
  keywords = ['deeplearning', 'pytorch', 'machinelearning'], # arbitrary keywords
  classifiers = ['Development Status :: 3 - Alpha',
		'Topic :: Deep Learning :: Machine Learning',
			],
)
