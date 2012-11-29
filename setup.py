#!/usr/bin/env python 
import os

from distutils.core import setup 

SCRIPT_DIR = os.path.dirname(__file__)
if SCRIPT_DIR == '':
    SCRIPT_DIR = '.'

scripts = filter(lambda x: not os.path.basename(x).startswith('.'), ['scripts/%s' % x for x in os.listdir('%s/scripts' % (SCRIPT_DIR,))])

setup(name = 'debgit', 
      version = '0.1', 
      description = "Tools to build deb packages with a Git-based workflow",
      author = "Roberto Aguilar", 
      author_email = "roberto.c.aguilar@gmail.com", 
      packages = ['debgit'], 
      long_description=open('README.md').read(),
      scripts=scripts,
      url='http://github.com/rca/reprepro_watch',
      license='LICENSE.txt'
)
