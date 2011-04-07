#!/usr/bin/python -tt
#
# test_basename.py - basename test suite
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
import unittest

from baseclass import RequiresBasename

class BasenameMissingOperandTestCase(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename),
                         "basename: missing operand\nTry `basename --help' for more information.")

class BasenameExtraOperandTestCase(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " a b c"),
                         "basename: extra operand `c'\nTry `basename --help' for more information.")

class BasenameTestA(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " d/f"), "f")

class BasenameTestB(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " /d/f"), "f")

class BasenameTestC(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " d/f/"), "f")

class BasenameTestD(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " d/f//"), "f")

class BasenameTestE(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " f"), "f")

class BasenameTestF(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " /"), "/")

class BasenameTestG(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " //"),
                         self._doubleSlash)

class BasenameTestH(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " ///"), "/")

class BasenameTestI(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " ///a///"), "a")

class BasenameTestJ(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " ''"), "")

class BasenameTestK(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " f.s .s"), "f")

class BasenameTestL(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs s"), "f")

class BasenameTestM(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs fs"), "fs")

class BasenameTestN(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs/ s"), "f")

class BasenameTestO(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename +
                                            " dir/file.suf .suf"), "file")

class BasenameTestP(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " // /"),
                         self._doubleSlash)

class BasenameTestQ(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " // //"),
                         self._doubleSlash)

class BasenameTestR(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs x"), "fs")

class BasenameTestS(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs ''"), "fs")

class BasenameTestT(RequiresBasename):
    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename + " fs/ s/"), "fs")
