#!/usr/bin/env python
#
# baseclass.py - base classes for all test cases
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

import glob
import imputil
import os
import sys
import tempfile
import unittest

class RequiresCommand(unittest.TestCase):
    def setUp(self):
        if os.path.isdir('src'):
            self._commandPath = os.path.realpath(os.getcwd() + "/src")
        elif os.path.isdir('../src'):
            self._commandPath = os.path.realpath(os.getcwd() + "/../src")
        else:
            raise RuntimeError("unable to find src subdirectory")

    def getCommand(self, cmd):
        return os.path.realpath(self._commandPath + "/" + cmd)

class RequiresBasename(RequiresCommand):
    def setUp(self):
        RequiresCommand.setUp(self)
        self._basename = self.getCommand("basename")

        s = os.stat("/")
        d = os.stat("//")
        if (s.st_dev == d.st_dev) and (s.st_ino == d.st_ino):
            self._doubleSlash = "/"
        else:
            self._doubleSlash = "//"

class RequiresCksum(RequiresCommand):
    def setUp(self):
        RequiresCommand.setUp(self)
        self._cksum = self.getCommand("cksum")
        (self._fd, self._testfile) = tempfile.mkstemp(prefix='cksum',
                                                      text=True)
        self._cmd = self._cksum + " " + self._testfile

    def tearDown(self):
        if self._testfile:
            os.unlink(self._testfile)

class RequiresGroups(RequiresCommand):
    def setUp(self):
        RequiresCommand.setUp(self)
        self._groups = self.getCommand("groups")

def loadModules(moduleDir, cls_pattern="TestCase",
                skip_list=["__init__", "baseclass"]):
    '''taken from pykickstart/tests/baseclass.py which was in turn
       taken from firstboot/loader.py
    '''

    # Guaruntee that __init__ is skipped
    if skip_list.count("__init__") == 0:
        skip_list.append("__init__")

    tstList = list()

    # Make sure moduleDir is in the system path so imputil works.
    if not moduleDir in sys.path:
        sys.path.insert(0, moduleDir)

    # Get a list of all *.py files in moduleDir
    moduleList = []
    lst = map(lambda x: os.path.splitext(os.path.basename(x))[0],
              glob.glob(moduleDir + "/*.py"))

    # Inspect each .py file found
    for module in lst:
        if module in skip_list:
            continue

        # Attempt to load the found module.
        try:
            found = imputil.imp.find_module(module)
            loaded = imputil.imp.load_module(module, found[0], found[1], found[2])
        except ImportError, e:
            print("Error loading module %s." % module)

        # Find class names that match the supplied pattern (default: "TestCase")
        beforeCount = len(tstList)
        for obj in loaded.__dict__.keys():
            if obj.endswith(cls_pattern):
                tstList.append(loaded.__dict__[obj])
        afterCount = len(tstList)

        # Warn if no tests found
        if beforeCount == afterCount:
            print("Module %s does not contain any test cases; skipping." % module)
            continue

    return tstList

# Run tests
if __name__ == "__main__":
    PyCoreUtilsTestSuite = unittest.TestSuite()

    cwd = os.getcwd()
    tstList = loadModules(os.path.join(cwd, "tests/"))
    for tst in tstList:
        PyCoreUtilsTestSuite.addTest(tst())

    unittest.main(defaultTest="PyCoreUtilsTestSuite")
