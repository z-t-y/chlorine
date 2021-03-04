from os import path
from codecs import open
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))

# get the long description from README.md
with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Chlorine')
