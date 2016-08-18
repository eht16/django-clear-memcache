# -*- coding: utf-8 -*-

from django_clear_memcache.clear import ClearMemcacheController
from django.core.management.base import BaseCommand


########################################################################
class Command(BaseCommand):

    help = ("Clear all keys from the configured default memcache server using the configured prefix")
    can_import_settings = True

    def handle(self, **options):
        verbosity = int(options.get("verbosity", 0))

        controller = ClearMemcacheController()
        result = controller.clear_cache()

        if verbosity >= 1:
            return result
