#!/usr/bin/env python
# coding=utf-8


from setuptools import find_packages, setup

from onepiece import __version__


setup(
    name='onepiece',
    version=__version__,
    description='One Piece',
    author='akun',
    author_email='6awkun@gmail.com',
    license='MIT License',
    url='https://github.com/akun/pm/tree/master/pm/onepiece',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'future>=0.16.0',
    ],
    extras_require={
        'test': [
            'coverage>=4.5',
            'httpretty>=0.8.14',
            'nose>=1.3.7',
        ],
    },
    test_suite='nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
