#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'troposhere>=2.5.0', 'cfn-macro-vpc-core', 'cfn-macro-vpc-subnets']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="John Mille",
    author_email='JohnPreston@users.noreply.github.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="CFN Macro VPC",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cfn_macro_vpc',
    name='cfn_macro_vpc',
    packages=find_packages(include=['cfn_macro_vpc']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/johnpreston/cfn_macro_vpc',
    version='0.1.0',
    zip_safe=False,
)
