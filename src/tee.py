#!/usr/bin/env python
#
# tee.py - tee(1) command written in Python
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

pyteever = (1, 0)

import getopt, sys
from pycoreutils.common import *
from pycoreutils.pytee import pytee
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])
	append, ignoreint = False, False
	help, version = False, False

	opts, args = [], []

	try:
		opts, args = getopt.getopt(sys.argv[1:], "ai",
		                           ["append", "ignore-interrupts",
		                            "help", "version"])
	except getopt.GetoptError:
		help = True
		
	for o, a in opts:
		if o in ("-a", "--append"):
			append = True
		if o in ("-i", "--ignore-interrupts"):
			ignoreint = True
		if o in ("--help"):
			help = True
		if o in ("--version"):
			version = True

	if help:
		try:
			from pycoreutils.usage import pytee_usage
			pytee_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif version:
		showversion(prog, pyteever)
	else:
		if ignoreint:
			import signal
			signal.signal(signal.SIGINT, signal.SIG_IGN)

		pytee(args + ['-'], append)
		sys.exit(0)

if __name__ == "__main__":
	main()
