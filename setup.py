
# coding: utf-8

val = []
with open('requirements.txt') as fp:
    for lines in fp:
        val.append(lines.split()) 

flatten = lambda l: [item for val in l for item in val] # to get imports 


from distutils.core import setup
setup(
  name = 'fastai',
  packages = ['fastai'], # this must be the same as the name above
  version = '0.4',
  author = 'Jeremy Howard, Rachel Thomas, Yannet Interian and many others',
  author_email = 'j@fast.ai',
  description = 'The fast.ai deep learning library, lessons, and tutorials',
  url = 'https://github.com/fastai/fastai.git', # use the URL to the github repo
  download_url = 'https://github.com/groverpr/fastai/archive/0.4.tar.gz', 

  install_requires= flatten(val), 

  keywords = ['deeplearning', 'pytorch', 'machinelearning'], # arbitrary keywords
  classifiers = ['Development Status :: 3 - Alpha'
			],
)
