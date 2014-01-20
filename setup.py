#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('./src')
from distutils.core import setup
from regexdict import __version__

setup(name='regexdict',
      version=__version__,
      description='Regex Dict',
      long_description=open("README.md").read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['regexdict'],
      package_dir={'regexdict': 'src/regexdict'},
      package_data={'regexdict': ['stuff']},
      license="MIT",
      platforms=["any"],
      url='https://github.com/solos/regexdict')
