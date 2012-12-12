# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Unit tests for profil in caro

"""
from django.test import TestCase
from django.conf import settings

class CachesTests(TestCase):  # pylint: disable-msg=R0904
    """
    The logs object

    """

    def SetUp(self):
        """setUp the tests
        """
        settings.CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                'LOCATION': '127.0.0.1:11211',
                'KEY_PREFIX': 'calo_tests_'
                }
            }

    def test_cache(self):

        import memcache
        from django.core.cache import cache

        key = "onair_title_foo"
        value = "from"
        prefix = settings.CACHES['default']['KEY_PREFIX']

        mc = memcache.Client(['127.0.0.1:11211'], debug=1)
        mc.set("%s:1:%s" % (prefix, key), value)

        self.assertEqual(cache.get(key), value)
