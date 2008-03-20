#!/usr/bin/env python
#
# sleep.py - sleep(1) command written in Python
# Copyright (C) 2007  Chris Lumens <clumens@redhat.com>
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

pysleepver = (1, 0)

import sys
from pycoreutils.common import *
from pycoreutils.pysleep import pysleep
from pycoreutils.pybasename import pybasename

def _help(prog):
	try:
		from pycoreutils.usage import pysleep_usage
		pysleep_usage(prog)
	except:
		print "Help screen is not available."

def main():
	prog = pybasename(sys.argv[0])

	if len(sys.argv) == 1 or sys.argv[1] == "--help":
		_help(prog)
		sys.exit(0)
	elif sys.argv[1] == "--version":
		showversion(prog, pysleepver)
	else:
		rc = pysleep(sys.argv[1])

		if rc == 1:
			print "%s: invalid time interval `%s'" % (prog, sys.argv[1])
			_help(prog)

		sys.exit(rc)

if __name__ == "__main__":
	main()
