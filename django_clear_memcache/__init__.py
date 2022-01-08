# -*- coding: utf-8 -*-

VERSION = (1, 4, 3)

default_app_config = 'django_clear_memcache.apps.ClearMemcacheConfig'

try:
    # Django 4.x
    from django.utils.translation import gettext_lazy as _
except ImportError:
    # Older Versions
    from django.utils.translation import ugettext_lazy as _
