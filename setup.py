from os import path
from codecs import open
from setuptools import setup, find_packages

basedir = path.abspath(path.dirname(__file__))

# get the long description from README.md
with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Chlorine',
    
    version='0.1.0',
    author='Fluorine Team',
    description='The core part of project Fluorine',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.github.com/rice0208/chlorine',

    license='GPL-3.0 License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    )
