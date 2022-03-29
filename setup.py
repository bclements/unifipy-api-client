#!/usr/bin/env python

from setuptools import setup

setup(name='unifipy-api-client',
      version='1.0',
      description='Client SDK for Ubiquity Networks UniFi controller',
      author='Brent Clements',
      author_email='brent.clements@gmail.com',
      url='https://github.com/bclements/unifipy-api-client',
      packages=['unifipy-api-client'],      
      classifiers=[],
      install_requires=['requests'],
      )
