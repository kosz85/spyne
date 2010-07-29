#!/usr/bin/env python
#
# soaplib - Copyright (C) Soaplib contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

import unittest

from suds.client import Client
from suds import WebFault

class TestSuds(unittest.TestCase):
    def setUp(self):
        self.client = Client("http://localhost:9753/?wsdl", cache=None)

    def test_enum(self):
        DaysOfWeekEnum = self.client.factory.create("DaysOfWeekEnum")

        val = DaysOfWeekEnum.Monday
        ret = self.client.service.echo_enum(val)

        assert val == ret

    def test_validation(self):
        non_nillable_class = self.client.factory.create("NonNillableClass")
        non_nillable_class.i = 6
        non_nillable_class.s = None

        try:
            ret = self.client.service.non_nillable(non_nillable_class)
            raise Exception("must fail")
        except WebFault, e:
            pass

    def test_echo_string(self):
        test_string = "OK"
        ret = self.client.service.echo_string(test_string)

        self.assertEquals(ret, test_string)

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(TestSuds)

if __name__== '__main__':
    unittest.TextTestRunner().run(suite())
