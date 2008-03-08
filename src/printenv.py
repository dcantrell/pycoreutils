#!/usr/bin/env python
#
# pyprintenv.py - pyprintenv(1) command written in Python
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
# Author: Chris Lumens <clumens@redhat.com>
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
