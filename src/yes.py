#!/usr/bin/env python
#
# yes.py - yes(1) command written in Python
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

pyyesver = (1, 0)

import sys
from pycoreutils.common import *
from pycoreutils.pyyes import pyyes
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])

	if len(sys.argv) == 1:
		pyyes()
		sys.exit(0)

	if sys.argv[1] == "--help":
		try:
			from pycoreutils.usage import pyyes_usage
			pyyes_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif sys.argv[1] == "--version":
		showversion(prog, pyyesver)
	else:
		tlist = []
		i = 1
		while i <= len(sys.argv):
			tlist.append(sys.argv[i])
			i = i + 1

		text = ' '.join(tlist)
		pyyes(text)

		sys.exit(0)

if __name__ == "__main__":
	main()
