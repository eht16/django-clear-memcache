# -*- coding: utf-8 -*-

# MemcachedUtility is loosely based on https://github.com/dlrust/python-memcached-stats

from django_clear_memcache.utility import MemcachedUtility
from django.conf import settings
from django.core.cache import cache, DEFAULT_CACHE_ALIAS
from django.core.exceptions import ImproperlyConfigured
from django.utils import six


########################################################################
class ClearMemcacheNoCacheFoundError(ImproperlyConfigured):
    pass


########################################################################
class ClearMemcacheController(object):

    #----------------------------------------------------------------------
    def __init__(self):
        self._servers = None
        self._host = None
        self._port = None
        self._cache_key_prefix = None
        self._keys = None
        self._init()

    #----------------------------------------------------------------------
    def _init(self):
        # support django-debug-toolbar which wraps the cache instance
        cache_ = getattr(cache, 'cache', cache)
        # check if we got a usable cache instance
        if not hasattr(cache_, '_lib'):
            raise ClearMemcacheNoCacheFoundError(u'Unknown memcached backend or no memcached backend found')

        # get cache key prefix
        self._cache_key_prefix = cache.key_prefix
        # LOCATION can be a string or a sequence
        server = settings.CACHES[DEFAULT_CACHE_ALIAS]['LOCATION']
        if isinstance(server, six.string_types):
            servers = server.split(';')
        else:
            servers = server

        self._servers = list()
        for server in servers:
            host, port = server.split(':')
            port = self._parse_port(port)
            if self._host == u'unix':
                # for now, ignore unix domain sockets
                continue
            self._servers.append((host, port))

    #----------------------------------------------------------------------
    def _parse_port(self, port):
        try:
            return int(port)
        except (ValueError, TypeError), e:
            raise ClearMemcacheNoCacheFoundError(u'Unable to parse port "%s": %e' % (port, e))

    #----------------------------------------------------------------------
    def keys(self, use_prefix=True, refresh=False):
        # cache keys per instance
        if self._keys is None or refresh:
            self._keys = list()
            for self._host, self._port in self._servers:
                try:
                    utility = MemcachedUtility(self._host, self._port)
                    utility.open()
                    # search for keys, according to the configured prefix
                    server_keys = utility.keys()
                    self._keys.extend(server_keys)
                finally:
                    utility.close()

        if use_prefix:
            keys = self._keys[:]  # copy
            for key in self._keys:
                if not key.startswith(self._cache_key_prefix):
                    keys.remove(key)
        else:
            keys = self._keys

        return keys

    #----------------------------------------------------------------------
    def clear_cache(self, use_prefix=True):
        if use_prefix:
            # iterate over all caches and delete single keys
            for self._host, self._port in self._servers:
                # clear this cache
                self._clear()
        else:
            # flush all caches
            for self._host, self._port in self._servers:
                # clear this cache
                self._flush()

    #----------------------------------------------------------------------
    def _clear(self):
        utility = MemcachedUtility(self._host, self._port)
        utility.open()
        try:
            for key in utility.keys():
                key = key.strip()
                if key.startswith(self._cache_key_prefix):
                    utility.delete(key)
        finally:
            utility.close()

    #----------------------------------------------------------------------
    def _flush(self):
        utility = MemcachedUtility(self._host, self._port)
        utility.open()
        try:
            utility.flush()
            # now iterate over all remaining keys and retrieve them to finally clear them from
            # the cache, otherwise they would still show up even if already flushed
            for key in utility.keys():
                utility.get(key)
        finally:
            utility.close()
