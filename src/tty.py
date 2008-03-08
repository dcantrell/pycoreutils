#!/usr/bin/env python
#
# tty.py - tty(1) command written in Python
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2.  This program is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY expressed or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.  You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA. Any Red Hat trademarks that are incorporated in the source code or
# documentation are not subject to the GNU General Public License and may
# only be used or replicated with the express permission of Red Hat, Inc.
#
# Author: David Cantrell <dcantrell@redhat.com>
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
