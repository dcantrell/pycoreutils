#!/usr/bin/env python
#
# dirname.py - dirname(1) command written in Python
# Copyright (C) 2007  David Cantrell <david.l.cantrell@gmail.com>
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

pydirnamever = (1, 0)

import sys
from pycoreutils.common import *
from pycoreutils.pydirname import pydirname
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])

	if len(sys.argv) == 1:
		print "%s: missing operand" % (prog,)
		print "Try `%s --help' for more information." % (prog,)
		sys.exit(1)

	if len(sys.argv) >= 3:
		print "%s: extra operand `%s'" % (prog, sys.argv[2],)
		print "Try `%s --help' for more information." % (prog,)
		sys.exit(1)

	if sys.argv[1] == "--help":
		try:
			from pycoreutils.usage import pydirname_usage
			pydirname_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif sys.argv[1] == "--version":
		showversion(prog, pydirnamever)
	else:
		print pydirname(sys.argv[1])
		sys.exit(0)

if __name__ == "__main__":
	main()
