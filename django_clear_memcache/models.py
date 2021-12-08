# -*- coding: utf-8 -*-

from django.db import models

try:
    #django 4.x
    from django.utils.translation import gettext_lazy as _
except ImportError:
    # Older Versions
    from django.utils.translation import ugettext_lazy as _


########################################################################
class ClearMemcache(models.Model):
    """This is a fake model, just to trick Django's admin to
       have an easy changelist view"""

    class Meta:
        managed = False
        app_label = 'django_clear_memcache'
        verbose_name = _('Clear Memcache')
        verbose_name_plural = _('Clear Memcache')
