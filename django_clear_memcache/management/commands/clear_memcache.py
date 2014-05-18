# -*- coding: utf-8 -*-

from django_clear_memcache.clear import ClearMemcacheController
from django.core.management.base import NoArgsCommand


########################################################################
class Command(NoArgsCommand):

    help = ("Clear all keys from the configured default memcache server using the configured prefix")
    can_import_settings = True

    def handle_noargs(self, **options):
        verbosity = int(options.get("verbosity", 0))

        controller = ClearMemcacheController()
        result = controller.clear_cache()

        if verbosity >= 1:
            return result
