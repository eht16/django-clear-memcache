# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


########################################################################
class ClearMemcache(models.Model):
    """This is a fake model, just to trick Django's admin to
       have an easy changelist view"""

    class Meta:
        managed = False
        app_label = u'django_clear_memcache'
        verbose_name = _(u'Clear Memcache')
        verbose_name_plural = _(u'Clear Memcache')
