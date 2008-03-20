#!/usr/bin/env python
#
# cksum.py - cksum(1) command written in Python
# Copyright (C) 2007  David Hilley <davidhi@cc.gatech.edu>
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

pycksumver = (1, 0)

import getopt, sys
from pycoreutils.common import *
from pycoreutils.pycksum import pycksum
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])
	help, version = False, False

	opts, args = [], []

	try:
		opts, args = getopt.getopt(sys.argv[1:], "",
		                            ["help", "version"])
	except getopt.GetoptError:
		help = True
		
	for o, a in opts:
		if o in ("--help"):
			help = True
		if o in ("--version"):
			version = True

	if help:
		try:
			from pycoreutils.usage import pycksum_usage
			pycksum_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif version:
		showversion(prog, pycksumver)
	else:
		t = pycksum(args)
		sys.exit(t)

if __name__ == "__main__":
	main()
