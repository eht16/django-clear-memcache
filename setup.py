# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

NAME = 'django-clear-memcache'
VERSION = '1.2.0'
DESCRIPTION = """\
Allow to clear Memcache items for the current site (according to the cache key prefix)
or even to clear the whole configured Memcache server.
The app integrates into Django's admin interface for easy use.
"""

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
    license = "BSD",
    include_package_data=True,
    zip_safe=False,
    requires=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
