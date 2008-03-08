#!/usr/bin/env python
#
# cksum.py - cksum(1) command written in Python
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
# Author: David Hilley <davidhi@cc.gatech.edu>
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
