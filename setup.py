# -*- coding: utf-8 -*-

import sys
from shutil import rmtree
from setuptools import setup, find_packages

NAME = 'django-clear-memcache'
VERSION = '1.3.0'
DESCRIPTION = """\
Allow to clear Memcache items for the current site (according to the cache key prefix)
or even to clear the whole configured Memcache server.
The app integrates into Django's admin interface for easy use.
"""

if 'bdist_wheel' in sys.argv:
    # Remove previous build dir when creating a wheel build, since if files have been removed
    # from the project, they'll still be cached in the build dir and end up as part of the
    # build, which is really neat!
    for directory in ('build', 'dist', 'django_clear_memcache.egg-info'):
        try:
            rmtree(directory)
        except:
            pass


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.rst').read(),
    version=VERSION,
    author='Enrico Tröger',
    author_email='enrico.troeger@uvena.de',
    url='https://github.com/eht16/django-clear-memcache',
    download_url='https://github.com/eht16/django-clear-memcache/archive/django-clear-memcache-%s.tar.gz' % VERSION,
    packages=find_packages(),
    license="BSD",
    include_package_data=True,
    zip_safe=False,
    requires=['django'],
    setup_requires=['flake8'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
