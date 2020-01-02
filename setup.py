# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# single-sourcing the version
with open(path.join(here, 'tradcal_gen/_version.py')) as f:
    exec(f.read())

install_requires = ''
with open('requirements.txt') as fp:
    install_requires = fp.read()

install_requires = install_requires.strip().splitlines()

setup(
    name='tradcal_gen',

    # Version single-sourced from tradcal_gen/_version.py
    version=__version__,

    description='Python app that generates a calendar in JSON or CSV format, based on rules',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Sanctifying-Time/tradcal-gen',

    # Author details
    author='Aaron Traas',
    author_email='aaron@traas.org',

    # Choose your license
    license='LGPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Religion',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
    ],

    keywords='Traditional Catholic Calendar',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    setup_requires=['babel'],
	install_requires = install_requires,

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'tradcal_gen=tradcal_gen:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/AaronTraas/Clash-Royale-Clan-Tools/issues',
        'Source': 'https://github.com/AaronTraas/Clash-Royale-Clan-Tools',
    },
)
