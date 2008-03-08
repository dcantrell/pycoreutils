#!/usr/bin/env python
#
# mkdir.py - mkdir(1) command written in Python
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

pymkdirver = (1, 0)

import getopt, sys
from pycoreutils.common import *
from pycoreutils.pymkdir import pymkdir
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])
	con = None
	mode = None
	parents, verbose = False, False
	help, version = False, False

	opts, args = [], []

	try:
		opts, args = getopt.getopt(sys.argv[1:], "Zm:pv",
		                           ["context=", "mode=", "parents",
		                            "verbose", "help", "version"])
	except getopt.GetoptError:
		help = True
                
	for o, a in opts:
		if o in ("-Z", "--context"):
			try:
				import selinux
				context = a
			except:
				print "SELinux support is not available on this system."
				sys.exit(1)
		if o in ("-m", "--mode"):
			mode = a
		if o in ("-p", "--parents"):
			parents = True
		if o in ("-v", "--verbose"):
			verbose = True
		if o in ("--help"):
			help = True
		if o in ("--version"):
			version = True

	if len(args) == 0 or help:
		try:
			from pycoreutils.usage import pymkdir_usage
			pymkdir_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif version:
		showversion(prog, pymkdirver)
	else:
		ret = pymkdir(args, mode, parents, verbose, con=context)
		sys.exit(ret)

if __name__ == "__main__":
	main()
