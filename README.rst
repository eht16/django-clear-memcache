Overview
========

Allow to clear Memcache items for the current site (according to the cache key prefix)
or even to clear the whole configured Memcache server.
The app integrates into Django's admin interface for easy use.


Installation
============

- Install:

    pip install django-clear-memcache

- Add `django_clear_memcache` to `INSTALLED_APPS`

- If not already done, configure `CACHES` to have a default cache
  with one of the supported Memcache backends (`django.core.cache.backends.memcached.*`)
  and set a `KEY_PREFIX`.

Usage
=====

Open the admin interface and find the new menu item "Clear Memcache".
There you can clear cache items for the configured `KEY_PREFIX` or
even the whole Memcache server.

Furthermore, you can list known items in the cache for the configured `KEY_PREFIX`.


Changes
=======

* 2015-08-16 - 1.1.1:
    * Case memcached port number to an integer
      (to fix connection errors in telnetlib)

* 2014-12-09 - 1.1.0:
    * Django 1.7 support
    * Find also namespaced jQuery

* 2014-05-24 - 1.0.1:
    * Include templates and static files

* 2014-05-18 - 1.0.0:
    * Initial release


License
=======

Copyright (c) 2014, Enrico Tröger
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name django-wakawaka nor the names of its contributors
      may be used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
