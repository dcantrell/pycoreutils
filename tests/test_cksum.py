#!/usr/bin/python -tt
#
# test_cksum.py - cksum test suite
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

import commands
import os
import string
import unittest

from baseclass import RequiresCksum

class CksumEmptyFileTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.close(self._fd)

    def runTest(self):
        output = "4294967295 0 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumATestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, "a")
        os.close(self._fd)

    def runTest(self):
        output = "1220704766 1 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumAbcTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, "abc")
        os.close(self._fd)

    def runTest(self):
        output = "1219131554 3 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumMessageDigestTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, "message digest")
        os.close(self._fd)

    def runTest(self):
        output = "3644109718 14 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumAlphabetTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, "abcdefghijklmnopqrstuvwxyz")
        os.close(self._fd)

    def runTest(self):
        output = "2713270184 26 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumAlphaNumericTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, string.letters + string.digits)
        os.close(self._fd)

    def runTest(self):
        output = "4086730865 62 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumDigitsTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, string.digits)
        os.close(self._fd)

    def runTest(self):
        output = "3648003736 10 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumA1KTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, 'a' * 1024)
        os.close(self._fd)

    def runTest(self):
        output = "2619405351 1024 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

class CksumB2KTestCase(RequiresCksum):
    def setUp(self):
        RequiresCksum.setUp(self)
        os.write(self._fd, 'b' * 2048)
        os.close(self._fd)

    def runTest(self):
        output = "2318161176 2048 " + self._testfile
        self.assertEquals(commands.getoutput(self._cmd), output)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CksumEmptyFileTestCase())
    suite.addTest(CksumATestCase())
    suite.addTest(CksumAbcTestCase())
    suite.addTest(CksumMessageDigestTestCase())
    suite.addTest(CksumAlphabetTestCase())
    suite.addTest(CksumAlphaNumericTestCase())
    suite.addTest(CksumDigitsTestCase())
    suite.addTest(CksumA1KTestCase())
    suite.addTest(CksumB2KTestCase())

    return suite

s = suite()
unittest.TextTestRunner(verbosity=2).run(s)
