__author__ = 'amitassaraf'
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, '..', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tchat',
    version='1.0.0',
    description='A chat server that is compatible with Slack client',
    long_description=long_description,
    url='https://github.com/amitassaraf/tchat',
    author='Amit Assaraf',
    author_email='soit48@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='slack server',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['rethinkdb', 'jsonpickle']
)