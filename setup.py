"""
------------------------------------------------------------------------------
COPYRIGHT/LICENSE.  This file is part of the XYZ package.  It is subject
to the license terms in the LICENSE file found in the top-level directory of
this distribution.  No part of the XYZ package, including this file, may be
copied, modified, propagated, or distributed except according to the terms
contained in the LICENSE file.
------------------------------------------------------------------------------
"""
# --- Imports

import os
import re
from setuptools import setup, find_packages


# --- Package requirements

SETUP_REQUIREMENTS = ['pytest-runner']

INSTALL_REQUIREMENTS = [
    'click',
    ]

TEST_REQUIREMENTS = [
    'coverage',
    'psutil',
    'pycodestyle',
    'pylint',
    'pytest>=3.7',
    'pytest-cov',
    'pytest-pycodestyle',
    'pytest-pylint',
    'pytest-xdist',
    ]
DEV_REQUIREMENTS = TEST_REQUIREMENTS + [
    'ipython',
    'radon',
    'sphinx',
    ]


# --- Package information

# Package root directory
PKG_ROOT_DIR = os.path.dirname(os.path.normcase(__file__))

# Version
with open(os.path.join(PKG_ROOT_DIR, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

# Authors and author email
with open(os.path.join(PKG_ROOT_DIR, 'AUTHORS')) as authors_file:
    AUTHORS = [line.strip() for line in authors_file.readlines()]
    if AUTHORS:
        AUTHOR_EMAIL = re.match('.*<(.*)>.*', AUTHORS[0]).group(1)
    else:
        AUTHOR_EMAIL = ''

    # Convert AUTHORS list to string
    AUTHORS = ', '.join(author.split('<')[0].strip() for author in AUTHORS)

# --- setup()

setup(
    # Package information
    name='PLACEHOLDER',
    version=VERSION,
    license='Apache Software License',
    author=AUTHORS,
    author_email=AUTHOR_EMAIL,
    description='PLACEHOLDER',
    long_description=open('README.markdown').read(),
    keywords='PLACEHOLDER',
    url='PLACEHOLDER',

    # Package construction
    packages=find_packages(),
    scripts=[],

    # Package requirements
    setup_requires=SETUP_REQUIREMENTS,
    install_requires=INSTALL_REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
        'test': TEST_REQUIREMENTS,
    }
)
