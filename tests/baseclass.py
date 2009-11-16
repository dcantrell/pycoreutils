#!/usr/bin/env python -tt
#
# baseclass.py - base class for all test cases
# Copyright (C) 2009  David Cantrell <david.l.cantrell@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

import os
import unittest

class RequiresCommand(unittest.TestCase):
    def setUp(self):
        self._commandPath = os.path.realpath(os.getcwd() + "/../src")

    def getCommand(self, cmd):
        return os.path.realpath(self._commandPath + "/" + cmd)
