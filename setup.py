#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='2captcha-python',
      version='1.1.0',
      description='Python module for easy integration with 2Captcha API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/2captcha/2captcha-python/',
      install_requires=['requests'],
      author='2Captcha',
      author_email='info@2captcha.com',
      packages=find_packages(include=['twocaptcha']),
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6')
