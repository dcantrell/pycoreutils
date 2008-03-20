#!/usr/bin/env python
#
# tty.py - tty(1) command written in Python
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

pyttyver = (1, 0)

import sys, posix
from pycoreutils.common import *
from pycoreutils.pytty import pytty
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])

	tty = pytty()

	if len(sys.argv) == 1:
		if tty is None:
			print "not a tty"
		else:
			print tty
		sys.exit(0)

	a = sys.argv[1]

	if a == "--help":
		try:
			from pycoreutils.usage import pytty_usage
			pytty_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif a == "--version":
		showversion(prog, pyttyver)
	elif a == '-s' or a == '--silent' or a == '--quiet':
		sys.exit(posix.isatty(tty))
	else:
		print "%s: extra operand `%s'" % (prog, sys.argv[1],)
		print "Try `%s --help' for more information." % (prog,)
		sys.exit(1)

if __name__ == "__main__":
	main()
