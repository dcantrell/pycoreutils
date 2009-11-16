#!/usr/bin/env python -tt
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
from baseclass import RequiresCommand

class BasenameTestCase(RequiresCommand):
    def setUp(self):
        RequiresCommand.__setUp__(self)
        self._basename = self.getCommand("basename")

        statSingle = os.stat("/")
        statDouble = os.stat("//")
        if (statSingle["st_dev"] == statDouble["st_dev"]) and \
           (statSingle["st_ino"] == statDouble["st_ino"]):
            self._doubleSlash = "/"
        else:
            self._doubleSlash = "//"

    def runTest(self):
        self.assertEqual(commands.getoutput(self._basename),
                         "basename: missing operand\nTry `basename --help' for more information.")
        self.assertEqual(commands.getoutput(self._basename + " a b c"),
                         "basename: extra operand `c'\nTry `basename --help' for more information.")

        tests = [("d/f", "f"),
                 ("/d/f", "f"),
                 ("d/f//", "f"),
                 ("f", "f"),
                 ("/", "/"),
                 ("//", self._doubleSlash),
                 ("///", "/"),
                 ("///a///", "a"),
                 ("''", ""),
                 ("f.s .s", "f"),
                 ("fs s", "f"),
                 ("fs fs", "fs"),
                 ("fs/ s", "f"),
                 ("dir/file.suf .suf", "file"),
                 ("// /", self._doubleSlash),
                 ("// //", self._doubleSlash),
                 ("fs x", "fs"),
                 ("fs ''", "fs"),
                 ("fs/ s/", "fs")]
        for (args, result) in tests:
            self.assertEqual(commands.getoutput(self._basename + " " + args),
                             result)

def suite():
    suite = unittest.TestSuite()
    suite.add(BasenameTestCase())
    return suite

s = suite()
unittest.TextTestRunner(verbosity=2).run(s)
