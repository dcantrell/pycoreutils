#!/usr/bin/env python
#
# pyprintenv.py - pyprintenv(1) command written in Python
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

pyprintenvver = (1, 0)

import sys
from pycoreutils.common import *
from pycoreutils.pyprintenv import pyprintenv
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])

	if len(sys.argv) == 1:
		(str, rc) = pyprintenv()
		print str
		sys.exit(rc)

	if sys.argv[1] == "--help":
		try:
			from pycoreutils.usage import pyprintenv_usage
			pyprintenv_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif sys.argv[1] == "--version":
		showversion(prog, pyprintenvver)
	else:
		(str, rc) = pyprintenv(sys.argv[1])
		if str != "":
			print str
		sys.exit(rc)

if __name__ == "__main__":
	main()
