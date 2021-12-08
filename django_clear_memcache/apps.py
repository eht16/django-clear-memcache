# -*- coding: utf-8 -*-

try:
    #django 4.x
    from django.utils.translation import gettext_lazy as _
except ImportError:
    # Older Versions
    from django.utils.translation import ugettext_lazy as _

try:
    # try to use AppConfig from Django 1.7, silently ignore on older versions
    from django.apps import AppConfig
except ImportError:
    pass
else:
    class ClearMemcacheConfig(AppConfig):
        name = 'django_clear_memcache'
        verbose_name = _("Clear Memcache")
