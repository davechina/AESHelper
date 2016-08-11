# -*-coding:utf-8 -*-

from setuptools import setup, find_packages

__author__ = "lqs"

setup(
    name="AESHelper",
    version="0.1",
    description="encrypt plain text or decrypt encrypted text using AES",
    author="lqs",
    url="https://github.com/davechina/AESHelper",
    license="MIT",
    packages=find_packages(),
    classifiers=['Programming Language :: Python :: 3.4'],
    keywords="aes",
    setup_requires=['pycrypto>=2.6.1']
)
