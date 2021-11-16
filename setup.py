

# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pymapcon',
    version='0.1.0',
    description='Sample package for Python Mapcon',
    long_description=readme,
    author='David Kim',
    author_email='agripda@gmail.com',
    url='https://github.com/agripda/pymapcon',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
