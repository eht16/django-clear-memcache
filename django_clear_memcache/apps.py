# -*- coding: utf-8 -*-

try:
    # try to use AppConfig from Django 1.7, silently ignore on older versions
    from django.apps import AppConfig
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    pass
else:
    class ClearMemcacheConfig(AppConfig):
        name = 'django_clear_memcache'
        verbose_name = _("Clear Memcache")
