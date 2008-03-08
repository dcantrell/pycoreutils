#!/usr/bin/env python
#
# groups.py - groups(1) command written in Python
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

pygroupsver = (1, 0)

import sys
from pycoreutils.common import *
from pycoreutils.pygroups import pygroups
from pycoreutils.pybasename import pybasename

def main():
	c = 0
	prog = pybasename(sys.argv[0])

	if len(sys.argv) == 1:
		print pygroups()
		sys.exit(0)

	if sys.argv[1] == "--help":
		c += 1
		try:
			from pycoreutils.usage import pygroups_usage
			pygroups_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif sys.argv[1] == "--version":
		c += 1
		showversion(prog, pygroupsnamever)
	else:
		userlist = []
		if len(sys.argv) - c > 0:
			i = c
			while i < len(sys.argv):
				userlist.append(sys.argv[i])
				i += 1
			print pygroups(userlist)
		sys.exit(0)

if __name__ == "__main__":
	main()
